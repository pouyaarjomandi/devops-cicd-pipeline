# 🚀 End-to-End CI/CD Pipeline with GitOps

A production-grade CI/CD pipeline built for a small e-commerce startup to automate the entire software delivery lifecycle — from code commit to production deployment — using Jenkins, Docker, Kubernetes, Helm, and ArgoCD.

## 📋 Project Overview

**Client:** Early-stage e-commerce startup (remote engagement)  
**Role:** Freelance DevOps Engineer  
**Duration:** 3 weeks  
**Objective:** Replace manual deployments with a fully automated, repeatable CI/CD pipeline using GitOps principles.

### Problem Statement

The development team was deploying manually via SSH and running into:
- Inconsistent environments between dev, staging, and production
- No automated testing — bugs were caught in production
- Deployments took ~30 minutes and caused downtime
- No rollback strategy

### Solution Delivered

Built a complete CI/CD pipeline that:
- Automatically builds, tests, and pushes Docker images on every commit
- Uses Helm charts with environment-specific values
- Deploys to Kubernetes via ArgoCD (GitOps)
- Includes code quality checks with SonarQube
- Sends Slack notifications on build status
- Achieves **zero-downtime deployments** with rolling updates

## 🏗️ Architecture

```
Developer → Git Push → Jenkins Pipeline
                          ├── Build Docker Image
                          ├── Run Unit Tests
                          ├── SonarQube Scan
                          ├── Push to Nexus Registry
                          └── Update Helm Values (Git)
                                    ↓
                              ArgoCD Detects Change
                                    ↓
                              Deploy to Kubernetes
                                ├── Dev Namespace
                                ├── Staging Namespace
                                └── Prod Namespace
```

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| CI/CD | Jenkins (Pipeline as Code) |
| Containerization | Docker |
| Orchestration | Kubernetes (Minikube / EKS) |
| Package Management | Helm 3 |
| GitOps | ArgoCD |
| Artifact Registry | Nexus Repository |
| Code Quality | SonarQube |
| Notifications | Slack Webhooks |
| Scripting | Bash, Python |
| Version Control | Git |

## 📁 Project Structure

```
.
├── app/                        # Sample Python Flask application
│   ├── app.py
│   ├── requirements.txt
│   ├── tests/
│   │   └── test_app.py
│   └── Dockerfile
├── jenkins/
│   ├── docker-compose.yml      # Jenkins + SonarQube + Nexus
│   ├── Jenkinsfile             # CI/CD Pipeline definition
│   └── config/
│       └── jenkins.yaml        # Jenkins Configuration as Code (JCasC)
├── helm/
│   └── myapp/
│       ├── Chart.yaml
│       ├── values.yaml
│       ├── values-dev.yaml
│       ├── values-staging.yaml
│       ├── values-prod.yaml
│       └── templates/
│           ├── deployment.yaml
│           ├── service.yaml
│           ├── ingress.yaml
│           └── hpa.yaml
├── argocd/
│   ├── install.yaml
│   └── application.yaml
├── k8s/
│   ├── namespace.yaml
│   └── secrets.yaml
├── scripts/
│   ├── setup.sh
│   └── cleanup.sh
└── docs/
    └── architecture.md
```

## 🚀 Getting Started

### Prerequisites

- Docker & Docker Compose
- Kubernetes cluster (Minikube or EKS)
- kubectl configured
- Helm 3 installed

### 1. Start CI/CD Infrastructure

```bash
# Start Jenkins, SonarQube, and Nexus
cd jenkins/
docker-compose up -d

# Access services:
# Jenkins:   http://localhost:8080
# SonarQube: http://localhost:9000
# Nexus:     http://localhost:8081
```

### 2. Configure Jenkins Pipeline

```bash
# Get Jenkins initial admin password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

### 3. Deploy ArgoCD

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f argocd/install.yaml
kubectl apply -f argocd/application.yaml
```

### 4. Access ArgoCD Dashboard

```bash
kubectl port-forward svc/argocd-server -n argocd 8443:443
# Username: admin
# Password: kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

## 📊 Results

| Metric | Before | After |
|--------|--------|-------|
| Deployment Time | ~30 min (manual) | ~5 min (automated) |
| Downtime per Deploy | 5-10 min | Zero (rolling updates) |
| Rollback Time | 30+ min | < 1 min (ArgoCD) |
| Test Coverage | 0% | 85% |
| Deployment Frequency | Weekly | Multiple times/day |

## 📝 Lessons Learned

- GitOps with ArgoCD simplifies rollbacks — just revert the Git commit
- Jenkins Configuration as Code (JCasC) makes Jenkins setup reproducible
- Helm value overrides per environment eliminate configuration drift
- SonarQube integration catches code quality issues before they reach production

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Pouya Arjmandiakram**  
DevOps / Cloud Engineer  
[LinkedIn](https://www.linkedin.com/in/pouya-arjomandi/) | [GitHub](https://github.com/pouyaarjomandi)