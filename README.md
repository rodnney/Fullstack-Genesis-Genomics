# Biotech Platform - Multi-Challenge Architecture

Plataforma completa com múltiplos desafios técnicos integrando diferentes stacks tecnológicas.

## 🏗️ Arquitetura

### Challenge 01 - DevOps (Proteomics Analysis)
- **Frontend**: Next.js (React/TypeScript)
- **Backend**: FastAPI (Python)
- **Infraestrutura**: AWS (EKS, RDS, S3, Batch)
- **Orquestração**: Kubernetes + Docker

### Challenge 02 - Genomics (Genesis Genomics)
- **Frontend**: Angular 16 + NgRx
- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL
- **State Management**: NgRx (Store, Effects, Entity)

## 📁 Estrutura do Projeto

```
biotech-platform/
├── challenge-01-devops/
│   ├── backend/          # API FastAPI
│   └── frontend/         # App Next.js
├── challenge-02-genomics/
│   ├── backend/          # API Django
│   └── frontend/         # App Angular
├── infra/
│   ├── main.tf          # Recursos AWS
│   └── k8s/            # Manifestos Kubernetes
├── docs/               # Documentação
└── docker-compose.yml  # Orquestração de todos os serviços
```

## 🚀 Execução Local

### Pré-requisitos

- Docker & Docker Compose
- Node.js 18+ (para desenvolvimento frontend)
- Python 3.11+ (para desenvolvimento backend)

### Iniciar Todos os Serviços

```powershell
# Subir todos os serviços
docker-compose up --build

# Acessar:
# Dashboard Principal: http://localhost:3000
# Challenge 01 (Proteomics): http://localhost:3000/dashboard
# Challenge 02 (Genomics): http://localhost:4200
# API FastAPI: http://localhost:8000
# API Django: http://localhost:8001
```

### Challenge 01 - Proteomics (FastAPI + Next.js)

```powershell
# Backend
cd challenge-01-devops/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Frontend
cd challenge-01-devops/frontend
npm install
npm run dev
```

### Challenge 02 - Genomics (Django + Angular)

```powershell
# Backend Django
cd challenge-02-genomics/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Importar dados (coloque siteA.txt e siteB.txt na raiz do backend)
python manage.py import_genes --siteA=siteA.txt --siteB=siteB.txt

# Frontend Angular
cd challenge-02-genomics/frontend
npm install
ng serve
```

## 🔧 Configuração de Desenvolvimento

### Pre-commit Hooks

```powershell
# Instale pre-commit
pip install pre-commit

# Configure os hooks
pre-commit install

# Execute manualmente (opcional)
pre-commit run --all-files
```

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz:

```env
# Desenvolvimento Local
DATABASE_URL=postgresql://admin_user:password@localhost:5432/biotech_db
S3_INPUT_BUCKET=biotech-input-local
S3_OUTPUT_BUCKET=biotech-output-local
AWS_REGION=us-east-1

# LocalStack
AWS_ENDPOINT_URL=http://localhost:4566
```

## 🏭 Deploy em Produção

### 1. Configuração AWS (Modo Demonstração)

O projeto está configurado para **não requerer AWS real**. Para demonstração:

```powershell
# Configure credenciais de demonstração
$env:AWS_ACCESS_KEY_ID="demo-access-key"
$env:AWS_SECRET_ACCESS_KEY="demo-secret-key"
$env:AWS_DEFAULT_REGION="us-east-1"

# Valide a infraestrutura
cd infra
terraform init
terraform validate
terraform plan -var="github_repository=rodnney/biotech-x-challenge"
```

### 2. GitHub Actions

Configure os seguintes secrets no GitHub (veja [docs/github-secrets-setup.md](docs/github-secrets-setup.md) para detalhes):

```
AWS_ROLE_ARN: arn:aws:iam::123456789012:role/biotech-x-platform-github-actions-role
ECR_REPOSITORY_BACKEND: biotech-backend
ECR_REPOSITORY_FRONTEND: biotech-frontend
EKS_CLUSTER_NAME: biotech-x-platform-cluster
```

**Nota**: Se os secrets não estiverem configurados, o workflow executará em modo demonstração (build apenas).

### 3. Deploy Manual

```powershell
# Build das imagens
docker build -t biotech-backend ./app/backend
docker build -t biotech-frontend ./app/frontend

# Deploy no Kubernetes (se configurado)
kubectl apply -f infra/k8s/application.yaml
```

## 📊 Monitoramento e Observabilidade

### Health Checks

- **Backend**: `GET /health`
- **Frontend**: `GET /api/health`

### Logs

```powershell
# Logs locais
docker-compose logs -f backend
docker-compose logs -f frontend

# Logs Kubernetes
kubectl logs -f deployment/biotech-backend
kubectl logs -f deployment/biotech-frontend
```

## 🧪 Testes

```powershell
# Backend
cd app/backend
pytest

# Frontend
cd app/frontend
npm test

# E2E (se configurado)
npm run test:e2e
```

## 📚 Documentação

- **API Docs**: http://localhost:8000/docs (Swagger)
- **Arquitetura**: [docs/index.md](docs/index.md)
- **GitHub Pages**: https://rodnney.github.io/biotech-x-challenge

## 🔒 Segurança

### Práticas Implementadas

- ✅ OIDC para GitHub Actions (sem access keys)
- ✅ Secrets scanning (detect-secrets)
- ✅ Dependency scanning
- ✅ Container security scanning
- ✅ Network policies (Kubernetes)
- ✅ IAM least privilege
- ✅ Encryption at rest (S3, RDS)

### Compliance

- **Retenção de dados**: 365 dias (input), 5 anos (output)
- **Backup**: Multi-AZ RDS, S3 versioning
- **Auditoria**: CloudTrail, VPC Flow Logs

## 🚨 Troubleshooting

### Problemas Comuns

**Docker não sobe:**
```powershell
docker-compose down
docker system prune -f
docker-compose up --build
```

**Terraform falha:**
```powershell
Remove-Item -Recurse -Force .terraform, .terraform.lock.hcl
terraform init
```

**Pre-commit falha:**
```powershell
pre-commit clean
pre-commit install
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch: `git checkout -b feature/nova-funcionalidade`
3. Commit: `git commit -m 'feat: adiciona nova funcionalidade'`
4. Push: `git push origin feature/nova-funcionalidade`
5. Abra um Pull Request

## 📄 Licença

Este projeto é parte de um desafio técnico e está disponível para fins educacionais.

---

## ✅ Resumo das Configurações

O projeto agora está otimizado para desenvolvimento no Windows:

- **Scripts PowerShell** para setup automático
- **Comandos Windows** em toda documentação
- **Docker Compose** simplificado sem dependências Linux
- **Terraform** configurado para validação local
- **Ambiente completo** sem necessidade de AWS real

**Para iniciar rapidamente:**
```powershell
.\scripts\setup-local.ps1
```

**Nota**: Este projeto foi desenvolvido como parte de um desafio técnico DevOps, focando em demonstrar conhecimentos de arquitetura cloud, IaC e boas práticas de desenvolvimento.
python -m pytest
app\frontend\npm run lint
infra\terraform fmt -check