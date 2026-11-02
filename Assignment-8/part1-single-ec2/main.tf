terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

# Find the latest Amazon Linux 2 image
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

# Security Group to allow web traffic
resource "aws_security_group" "app_sg" {
  name        = "assignment8-part1-sg"
  description = "Allow SSH + Flask(5000) + Express(3000)"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # SSH
  }
  ingress {
    from_port   = 3000
    to_port     = 3000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Express
  }
  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Flask
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# The EC2 Instance
resource "aws_instance" "app" {
  ami                    = data.aws_ami.amazon_linux.id
  instance_type          = "t3.micro" # Free tier eligible
  vpc_security_group_ids = [aws_security_group.app_sg.id]

  # This is where we inject the script!
  user_data = file("${path.module}/user_data.sh")

  tags = {
    Name = "Assignment8-Single-EC2"
  }
}

# Output the IP address so we can find it
output "public_ip" {
  value = aws_instance.app.public_ip
}