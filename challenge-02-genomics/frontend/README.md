# Genesis Genomics - Frontend Angular

Interface moderna e reativa para exploração de banco de dados genômicos, utilizando Angular 16 e gerenciamento de estado avançado com NgRx.

## 🛠️ Tecnologias
- Angular 16
- NgRx (Store, Effects, Entity)
- RxJS & TypeScript
- Material Design (ou CSS moderno)

## 🚀 Configuração Local

Siga os passos abaixo para rodar o frontend em ambiente de desenvolvimento:

1. **Instale as dependências:**
   ```powershell
   npm install
   ```

2. **Certifique-se de que o backend está rodando:**
   O frontend espera a API em [http://localhost:8001/api/genes/](http://localhost:8001/api/genes/). Se necessário, ajuste o `apiUrl` em `src/app/services/gene.service.ts`.

3. **Inicie o servidor de desenvolvimento:**
   ```powershell
   npm start
   # ou
   ng serve
   ```
   Acesse a aplicação em [http://localhost:4200](http://localhost:4200)

## 🧪 Testes e Build

- **Rodar testes unitários:** `ng test`
- **Gerar build de produção:** `ng build --configuration production`

---

## 📂 Arquitetura do Estado (NgRx)
- `store/`: Centralização da lógica de dados.
  - `actions`: Intenções de mudança.
  - `reducers`: Mudanças puras no estado.
  - `effects`: Lógica assíncrona (chamadas de API).
  - `selectors`: Consultas otimizadas ao estado.
