# Genesis Genomics - Backend Django

API REST robusta para gerenciamento e consulta de dados genômicos.

## 🛠️ Tecnologias
- Python 3.11+
- Django 4.2
- Django REST Framework
- PostgreSQL

## 🚀 Configuração Local

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

1. **Crie e ative o ambiente virtual:**
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Instale as dependências:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente:**
   ```powershell
   copy .env.example .env
   ```

4. **Prepare o Banco de Dados:**
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Importe os Dados Genômicos:**
   Garanta que os arquivos `siteA.txt` e `siteB.txt` estão na raiz desta pasta.
   ```powershell
   python manage.py import_genes --siteA=siteA.txt --siteB=siteB.txt
   ```

6. **Inicie o Servidor:**
   ```powershell
   python manage.py runserver
   ```
   A API estará disponível em [http://localhost:8001/api/genes/](http://localhost:8001/api/genes/)

---

## 📂 Estrutura Principal
- `core/`: Configurações de projeto e segurança.
- `genes/`: Lógica de negócio, modelos Genômicos e Serializers.
  - `management/commands/`: Scripts de CLI para processamento de arquivos.
