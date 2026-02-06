# 🔬 Challenge 01 - Proteomics Analysis (DevOps)

Este desafio foca na infraestrutura, automação de pipelines e orquestração de serviços para uma plataforma de análise proteômica.

## 🛠️ Stack Tecnológica

- **Backend:** FastAPI (Python 3.11)
- **Frontend:** Next.js (React/TypeScript)
- **Infraestrutura:** Terraform (IaC), Docker & Kubernetes (LocalStack)
- **Serviços AWS Simulados:** EKS, S3, RDS, IAM, STS.

## 🚀 Configuração Local

### Pré-requisitos
- Docker & Docker Compose
- Terraform (opcional, para testes de infra)

### Como rodar
A forma recomendada é através do `docker-compose.yml` na raiz do projeto:
```powershell
docker-compose up --build
```

### Componentes Individuais
Caso deseje rodar manualmente para desenvolvimento:

#### Backend (FastAPI)
1. Acesse `challenge-01-devops/backend`.
2. Configure o ambiente virtual e instale `requirements.txt`.
3. Rode: `uvicorn main:app --reload`.

#### Frontend (Next.js)
1. Acesse `challenge-01-devops/frontend`.
2. Instale dependências: `npm install`.
3. Rode: `npm run dev`.

---

## 🏗️ Infraestrutura e CI/CD

### Terraform
Os arquivos em `/infra` definem a infraestrutura necessária na AWS. Para validar localmente:
```powershell
cd infra
terraform init
terraform validate
```

### GitHub Actions
O repositório contém workflows para:
- Build e Push de imagens Docker (ECR).
- Linting e Testes automatizados.
- Deploy (simulado) no EKS cluster.

---

## 🧪 Testes
Para rodar os testes de backend:
```powershell
cd challenge-01-devops/backend
pytest
```
