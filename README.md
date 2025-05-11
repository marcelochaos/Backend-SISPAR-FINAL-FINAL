# 🧩 API para Gestão de Colaboradores e Reembolsos
Este projeto foi desenvolvido com Flask e tem como objetivo gerenciar colaboradores e controlar solicitações de reembolso. A API oferece recursos como cadastro, login, atualização de dados dos colaboradores e operações relacionadas a reembolsos.

## ⚙️ Tecnologias Utilizadas
🐍 Python 3.x

🔥 Flask

🧬 SQLAlchemy

🗂️ Flask-Session

🔐 Bcrypt

📘 Flasgger (para documentação Swagger)

🗄️ Banco de dados: MySQL, PostgreSQL ou SQLite




🧑‍💼 Funcionalidades

### 👤 Colaboradores

- 🙋‍♂️ Colaboradores
GET /colaborador/todos-colaboradores
🔎 Lista todos os colaboradores cadastrados.

POST /colaborador/cadastrar
➕ Cadastra um novo colaborador (com senha criptografada e verificação de e-mail único).

PUT /colaborador/atualizar/<id_colaborador>
🛠️ Atualiza os dados de um colaborador (mock).

POST /colaborador/login
🔑 Realiza login e inicia uma sessão.

GET /colaborador/perfil
👁️‍🗨️ Retorna as informações do colaborador autenticado.

---

###  💰 Reembolsos
POST /colaborador/reembolsos
📝 Registra uma nova solicitação de reembolso.

GET /colaborador/reembolsos/<num_prestacao>
📄 Visualiza um reembolso pelo número da prestação.

GET /colaborador/reembolsos
📋 Lista todas as solicitações.

GET /colaborador/reembolsos/<id>
🔍 Consulta um reembolso específico por ID.

---

## 🛠️ Como Rodar o Projeto

1. Clone o repositório:
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio

2. Crie e ative um ambiente virtual:
  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate     # Windows

3. Instale as dependências:
  pip install -r requirements.txt

4. Configure o banco de dados no arquivo app.py ou em um .env.

5. Execute o servidor:
  flask run
6. Acesse a documentação Swagger em:
   http://localhost:5000/apidocs/