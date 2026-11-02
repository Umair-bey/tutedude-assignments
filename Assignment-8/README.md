# Assignment 8 - Terraform (AWS Provisioning)

Deploy a full-stack application (**Flask backend** + **Express frontend**) on AWS using **Terraform** across three distinct architectural patterns.

## 📋 Stack

| Component | Technology | Port | Infrastructure |
|-----------|-----------|------|----------------|
| Backend | Flask (Python 3.9) | 5000 | EC2 / ECS Fargate |
| Frontend | Express (Node.js 16) | 3000 | EC2 / ECS Fargate |
| Provisioning | Terraform | — | Infrastructure as Code (IaC) |
| Container Registry | AWS ECR | — | Docker image storage |
| Orchestration | AWS ECS | — | Fargate (Serverless) |
| Load Balancing | AWS ALB | 80 | Application routing |

## 📁 Project Structure

```
Assignment-8/
├── part1-single-ec2/
│   ├── main.tf
│   ├── user_data.sh
│   └── README.md (optional)
├── part2-two-ec2s/
│   ├── main.tf
│   ├── backend.sh
│   ├── frontend.sh
│   └── README.md (optional)
├── part3-ecs-ecr/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── backend/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   └── frontend/
│       ├── server.js
│       ├── package.json
│       └── Dockerfile
└── README.md
```

## 🏗️ Architecture (Three Parts)

### Part 1: Single EC2 Instance
Both Flask and Express run on a single EC2 instance using a `user_data` bash script to install dependencies and start the apps.
```text
Internet → EC2 Instance (t3.micro)
              ├── Flask (Port 5000)
              └── Express (Port 3000)
```

### Part 2: Two Separate EC2 Instances (Custom VPC)
A custom VPC with a public subnet, Internet Gateway, and route tables. Two EC2 instances are launched. The Express frontend communicates with the Flask backend securely via the backend's Private IP.
```text
Internet → Frontend EC2 (Port 3000)
                ↓ (Private IP communication)
           Backend EC2 (Port 5000)
```

### Part 3: ECS Fargate + ECR + ALB
A fully containerized, serverless architecture. Docker images are pushed to ECR, ECS Fargate runs the containers, and an Application Load Balancer routes traffic.
```text
Internet → Application Load Balancer (Port 80)
              ├── Route "/" → Frontend ECS Task (Port 3000)
              └── Route "/api/*" → Backend ECS Task (Port 5000)
```

## ✅ Prerequisites

- **Terraform** (v1.9.8+) installed and added to PATH
- **AWS CLI** configured (`aws configure`) with `AmazonEC2FullAccess` and `IAMFullAccess`
- **Docker Desktop** running (required for Part 3)
- An existing **EC2 Key Pair** (optional, for SSH into Part 1/2 instances)

## 🚀 Step-by-Step Deployment

### General Workflow (For any part)
Navigate into the specific folder (e.g., `cd part3-ecs-ecr`) and run:
```powershell
terraform init
terraform validate
terraform plan
terraform apply --auto-approve
```

### Part 1: Single EC2
```powershell
cd part1-single-ec2
terraform init
terraform apply --auto-approve
# Access via the public IP output on ports 5000 and 3000
```

### Part 2: Two EC2s (Custom VPC)
```powershell
cd part2-two-ec2s
terraform init
terraform apply --auto-approve
# Access the frontend on port 3000. Click the /api link to test backend connectivity.
```

### Part 3: ECS, ECR, and ALB
This part requires building and pushing Docker images after the infrastructure is created.

**1. Provision Infrastructure:**
```powershell
cd part3-ecs-ecr
terraform init
terraform apply --auto-approve
```

**2. Authenticate Docker to ECR:**
```powershell
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 117647030291.dkr.ecr.ap-south-1.amazonaws.com
```

**3. Build and Push Backend:**
```powershell
cd backend
docker build -t assignment8-p3-backend .
docker tag assignment8-p3-backend:latest "117647030291.dkr.ecr.ap-south-1.amazonaws.com/assignment8-p3-backend:latest"
docker push "117647030291.dkr.ecr.ap-south-1.amazonaws.com/assignment8-p3-backend:latest"
cd ..
```

**4. Build and Push Frontend:**
```powershell
cd frontend
docker build -t assignment8-p3-frontend .
docker tag assignment8-p3-frontend:latest "117647030291.dkr.ecr.ap-south-1.amazonaws.com/assignment8-p3-frontend:latest"
docker push "117647030291.dkr.ecr.ap-south-1.amazonaws.com/assignment8-p3-frontend:latest"
cd ..
```

**5. Force ECS to Pull New Images:**
*(Because Terraform doesn't automatically detect updated Docker tags)*
```powershell
terraform apply -replace="aws_ecs_task_definition.backend" -replace="aws_ecs_task_definition.frontend" --auto-approve
```

**6. Access the Application:**
Wait 2-3 minutes for the ECS tasks to stabilize. Grab the `alb_dns_name` from the Terraform output and open it in your browser.

## 🧹 Cleanup

To avoid ongoing AWS charges (especially for the ALB and Fargate in Part 3), you must destroy the resources.

```powershell
# Run this inside each part's folder
terraform destroy --auto-approve
```

If `terraform destroy` hangs on the Internet Gateway, manually detach and delete the IGW and VPC from the AWS Console.

## 🐛 Troubleshooting

### `Error: Invalid function argument: vars map does not contain key...`
Terraform is trying to evaluate JavaScript template literals (`${...}`) inside your `.sh` files. Fix this by using the `replace()` function in `main.tf` or escaping the variables using `$${...}`.

### `CannotPullContainerError: pull image manifest has been retried...`
ECS is trying to pull an image that doesn't exist in ECR yet. Build, tag, and push your Docker images to ECR first, then force a new ECS deployment.

### `UnauthorizedOperation: not authorized to perform: ec2:TerminateInstances`
Your `cli-user` lacks IAM permissions. Attach the `AmazonEC2FullAccess` and `IAMFullAccess` policies to your IAM user in the AWS Console.

### ECS is running old code even after `docker push`
ECS does not automatically detect when a `:latest` tag is overwritten. You must force a new task definition revision by running:
`terraform apply -replace="aws_ecs_task_definition.backend" -replace="aws_ecs_task_definition.frontend" --auto-approve`

## 🎓 Key Learnings

1. **Infrastructure as Code (IaC)** — Writing declarative HCL to provision AWS resources.
2. **Custom VPC Networking** — Subnets, Route Tables, Internet Gateways, and Security Groups.
3. **Bash Scripting for Automation** — Using `user_data` to bootstrap EC2 instances.
4. **Docker & AWS ECR** — Building images, tagging, and pushing to Elastic Container Registry.
5. **AWS ECS Fargate** — Running serverless containers without managing underlying servers.
6. **Application Load Balancing** — Routing traffic based on URL paths (`/` vs `/api/*`).
7. **Terraform State Management** — Handling state files and forcing task definition replacements.

## 📚 References

- [Terraform AWS Provider Docs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [AWS ECS Documentation](https://docs.aws.amazon.com/ecs/)
- [AWS ECR Documentation](https://docs.aws.amazon.com/ecr/)
- [Terraform Docs](https://developer.hashicorp.com/terraform/docs)

## 👤 Author

**Umair Khan** 
DevOps Course— Tutedude