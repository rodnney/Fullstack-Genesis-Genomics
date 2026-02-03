# Configuração de Secrets do GitHub

Este documento explica como configurar os secrets necessários para o GitHub Actions funcionar corretamente.

## Secrets Obrigatórios para Deploy Real

Para fazer deploy real na AWS, configure os seguintes secrets no GitHub:

### 1. AWS_ROLE_ARN
```
arn:aws:iam::123456789012:role/biotech-x-platform-github-actions-role
```

### 2. ECR_REPOSITORY_BACKEND
```
biotech-backend
```

### 3. ECR_REPOSITORY_FRONTEND
```
biotech-frontend
```

### 4. EKS_CLUSTER_NAME
```
biotech-x-platform-cluster
```

## Como Configurar os Secrets

1. Vá para o seu repositório no GitHub
2. Clique em **Settings** → **Secrets and variables** → **Actions**
3. Clique em **New repository secret**
4. Adicione cada secret com o nome e valor correspondente

## Modo Demonstração

Se você não tem AWS configurada, o workflow automaticamente executará em modo demonstração:
- Fará build das imagens Docker
- Validará o Terraform
- Não tentará fazer deploy real

## Configuração OIDC (Recomendado)

Para usar OIDC em vez de access keys:

1. Configure o IAM Role na AWS com trust policy para GitHub
2. Adicione apenas o `AWS_ROLE_ARN` nos secrets
3. O workflow usará OIDC automaticamente

### Exemplo de Trust Policy para OIDC:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::123456789012:oidc-provider/token.actions.githubusercontent.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
          "token.actions.githubusercontent.com:sub": "repo:seu-usuario/biotech-x-challenge:ref:refs/heads/main"
        }
      }
    }
  ]
}
```

## Troubleshooting

### Erro: "The security token included in the request is invalid"

**Causa**: Credenciais AWS inválidas ou expiradas

**Solução**:
1. Verifique se todos os secrets estão configurados corretamente
2. Confirme que o IAM Role existe e tem as permissões necessárias
3. Para OIDC, verifique se o trust policy está correto

### Workflow não executa

**Causa**: Secrets não configurados

**Solução**: O workflow agora tem dois modos:
- **Demo**: Executa quando `AWS_ROLE_ARN` não está configurado
- **Deploy**: Executa quando `AWS_ROLE_ARN` está configurado