# Assignment 7 - Kubernetes Deployment

Deploy a full-stack application (**Flask frontend** + **Express backend**) on a local **Minikube** cluster.

## 📋 Stack

| Component | Technology | Port | Service Type |
|-----------|-----------|------|--------------|
| Frontend | Flask (Python 3.10) | 5000 | NodePort |
| Backend | Express (Node.js 18) | 3000 | ClusterIP |
| Orchestration | Kubernetes (Minikube) | — | — |

## 📁 Project Structure

```
Assignment-7/
├── backend/
│   ├── Dockerfile
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── package.json
│   └── server.js
├── frontend/
│   ├── Dockerfile
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
├── screenshots/
├── Kubernetes_UmairKhan.docx
└── README.md
```

## 🏗️ Architecture

```
Browser → frontend-service (NodePort:5000) → Flask Pod
                                              ↓
                            http://backend-service:3000
                                              ↓
                            backend-service (ClusterIP) → Express Pod
```

Kubernetes internal DNS resolves `backend-service` to the correct pod IP — no hardcoded IPs.

## ✅ Prerequisites

- **Docker Desktop** (v29.8.2+)
- **Minikube** (v1.39.0+)
- **kubectl** (v1.32.2+)

## 🚀 Step-by-Step Deployment

### 1. Start Minikube

```powershell
minikube start --driver=docker
minikube status
kubectl get nodes
```

### 2. Build Images Inside Minikube

> ⚠️ **Important on Windows:** `minikube docker-env | Invoke-Expression` fails with
> `SSH_AGENT_START: starting an SSH agent on Windows is not yet supported`.
>
> Use the built-in `minikube image build` command instead — it builds directly inside
> Minikube's Docker daemon, no env changes needed.

```powershell
# Backend
cd backend
minikube image build -t backend:v1 .
cd ..

# Frontend
cd frontend
minikube image build -t frontend:v1 .
cd ..

# Verify both images exist inside Minikube
minikube image ls | Select-String "backend|frontend"
```

### 3. Deploy to Kubernetes

```powershell
kubectl apply -f backend/deployment.yaml
kubectl apply -f backend/service.yaml
kubectl apply -f frontend/deployment.yaml
kubectl apply -f frontend/service.yaml
```

### 4. Verify Deployment

```powershell
kubectl get pods
kubectl get deployments
kubectl get services
kubectl get all
```

Expected: **4 pods Running** (2 backend + 2 frontend), both deployments `2/2` ready.

### 5. Access the Application

```powershell
minikube service frontend-service --url
```

Open the printed URL (e.g. `http://127.0.0.1:55113`) in a browser.

You should see:

> **Frontend (Flask) on Kubernetes 🚀**
> Backend says:
> **Hello from Express Backend on Kubernetes!**
> Status: success

> ⚠️ Keep the terminal window open — Minikube's Docker driver on Windows holds
> a tunnel through that terminal. Closing it kills the URL (cluster keeps running).

### 6. View the Kubernetes Dashboard (Optional)

```powershell
minikube dashboard
```

## 🧹 Cleanup

```powershell
kubectl delete -f backend/
kubectl delete -f frontend/
minikube stop
```

To fully delete the cluster:
```powershell
minikube delete
```

## 🐛 Troubleshooting

### `dockerfile parse error on line 1: unknown instruction: '@`

Files created via PowerShell here-strings were written with the terminator `'@`
as the first line. Fix by stripping the first line if it equals `'@`:

```powershell
$files = @(
  "backend\Dockerfile","backend\deployment.yaml","backend\service.yaml",
  "backend\package.json","backend\server.js",
  "frontend\Dockerfile","frontend\deployment.yaml","frontend\service.yaml",
  "frontend\requirements.txt","frontend\app.py","frontend\templates\index.html"
)
foreach ($f in $files) {
    $lines = [System.IO.File]::ReadAllLines($f)
    if ($lines[0].Trim() -match "^'@") {
        $lines = $lines[1..($lines.Count-1)]
        [System.IO.File]::WriteAllLines($f, $lines)
        Write-Host "Fixed: $f"
    }
}
```

### `minikube docker-env` fails with SSH agent error

Use `minikube image build` instead (see Step 2 above).

### Pods in `ImagePullBackOff`

Ensure `imagePullPolicy: Never` is set in both `deployment.yaml` files
(images are built inside Minikube, not pulled from a registry).

### Pre-commit Hook (Bonus DevOps Practice)

A Git pre-commit hook at `.git/hooks/pre-commit` scans staged files for stray
`'@` markers and blocks the commit if found:

```sh
#!/bin/sh
BAD=""
for f in $(git diff --cached --name-only --diff-filter=ACM); do
  if [ -f "$f" ]; then
    if head -n 1 "$f" | grep -q "^'@"; then
      BAD="$BAD\n  - $f (line 1)"
    fi
  fi
done
if [ -n "$BAD" ]; then
  echo "Commit blocked: stray PowerShell here-string marker found in:"
  printf "%b\n" "$BAD"
  exit 1
fi
exit 0
```

## 🎓 Key Learnings

1. **Containerization** — Dockerfiles for Node.js and Python apps
2. **Kubernetes Manifests** — Deployments + Services (ClusterIP, NodePort)
3. **Service Discovery** — Pods reach each other by service DNS name
4. **Minikube on Windows** — `minikube image build` is the reliable approach
5. **Byte-level Debugging** — Fixed malformed files by inspecting raw bytes
6. **Pre-commit Hooks** — Automated safety net to prevent broken commits

## 📚 References

- [Kubernetes Docs](https://kubernetes.io/docs/)
- [Minikube Docs](https://minikube.sigs.k8s.io/docs/)
- [Docker Docs](https://docs.docker.com/)

## 👤 Author

**Umair Khan** — Tutedude DevOps Course
