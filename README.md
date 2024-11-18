

# **Sistema de Atendimento para Clínica Médica**

## **Descrição**
Este projeto é um sistema de gestão para clínicas médicas, desenvolvido para facilitar o gerenciamento de pacientes, médicos e consultas. O sistema inclui funcionalidades como cadastro de pacientes, agendamento de consultas e gerenciamento de prontuários, tudo integrado a um banco de dados SQLite.

---

## **Funcionalidades**
- Cadastro e listagem de pacientes.
- Edição e exclusão de registros de pacientes.
- Cadastro de médicos (a ser implementado).
- Agendamento e gerenciamento de consultas (a ser implementado).
- Relatórios de consultas e faturamento (planejado).

---

## **Tecnologias Utilizadas**
- **Backend**: Python com Flask.
- **Frontend**: HTML, CSS, e JavaScript.
- **Banco de Dados**: SQLite.
- **Migração de Banco**: Flask-Migrate.

---

## **Pré-requisitos**
- Python 3.10 ou superior.
- Virtualenv (opcional, mas recomendado).

---

## **Instalação**
1. Clone o repositório:
  
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt**
   ```

4. Configure o banco de dados:
   ```bash
   flask db init
   flask db migrate -m "Criação inicial"
   flask db upgrade
   ```

5. Execute o servidor:
   ```bash
   python app.py
   ```

6. Acesse o sistema no navegador:
   ```
   http://127.0.0.1:5000/
   ```

---

## **Como Usar**
### **Pacientes**
1. Navegue até `/pacientes` para:
   - Cadastrar novos pacientes.
   - Listar, editar ou excluir pacientes existentes.

### **Consultas**
1. (Funcionalidade planejada) Navegue até `/agendamentos` para agendar e visualizar consultas.


## **Estrutura do Projeto**
```
service/
├── app.py                # Arquivo principal da aplicação
├── extensions.py         # Configuração de extensões
├── models.py             # Modelos de banco de dados
├── controllers/          # Lógica dos controladores
│   ├──
    ├──paciente_controller.py
│   └── 
├── templates/            # Templates HTML
│   ├── index.html
│   ├── 
│   └── 
├── static/               # Arquivos estáticos (CSS, JS)
├── migrations/           # Migrações do banco de dados
├── clinic.db             # Arquivo SQLite 
└── README.md             # Documentação




