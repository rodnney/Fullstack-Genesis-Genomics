# 🧬 Challenge 02 - Genesis Genomics

O **Genesis Genomics** é um explorador de dados genômicos que permite o cruzamento de informações de múltiplas fontes biológicas, oferecendo uma interface reativa e performática.

## 🛠️ Stack Tecnológica

- **Backend:** Django 4.2 + Django REST Framework (DRF)
- **Frontend:** Angular 16 + NgRx (Store, Effects, Entity)
- **Banco de Dados:** PostgreSQL 14
- **Linguagens:** Python 3.11, TypeScript

## 🚀 Configuração Local

### 1. Via Docker (Recomendado)
Execute na raiz do monorepo:
```powershell
docker-compose up --build
```

### 2. Manual (Desenvolvimento)

#### Backend (Django)
1. Acesse `challenge-02-genomics/backend`.
2. Crie e ative o ambiente virtual.
3. Instale as dependências: `pip install -r requirements.txt`.
4. Execute as migrações: `python manage.py migrate`.
5. Inicie o servidor: `python manage.py runserver 8001`.

#### Frontend (Angular)
1. Acesse `challenge-02-genomics/frontend`.
2. Instale as dependências: `npm install`.
3. Inicie o servidor: `ng serve`. Acesse em [http://localhost:4200](http://localhost:4200).

---

## 💾 Engenharia de Dados (Importação)

O sistema possui um comando customizado para importar e cruzar dados de dois arquivos (`siteA.txt` e `siteB.txt`).

**Comando de Importação:**
```powershell
python manage.py import_genes --siteA=siteA.txt --siteB=siteB.txt
```

*Nota: Se estiver rodando via Docker, use:*
```powershell
docker exec -it genomics-backend-django python manage.py import_genes --siteA=siteA.txt --siteB=siteB.txt
```

---

## 📂 Estrutura do Projeto
- `backend/genes/`: Contém os modelos e a lógica de importação.
- `frontend/src/app/store/`: Gerenciamento de estado global via NgRx.
- `frontend/src/app/components/`: Componentes reativos (Lista de Genes e Filtros).
