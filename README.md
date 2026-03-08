

🎯 Objetivo da Aula
Ensinar os fundamentos de:


Criação de uma aplicação web com Flask

Rotas (@app.route)

Uso de HTTP POST

Manipulação de dados em memória

Templates HTML com Jinja2

Formulários HTML integrados ao backend

🧠 Como a aplicação funciona
As tarefas (TODOs) são armazenadas em memória, usando uma lista Python

Cada tarefa possui:

id (inteiro incremental)

text (texto da tarefa)

done (se está concluída ou não)

Ao reiniciar o servidor, os dados são perdidos

O HTML é renderizado diretamente no Python usando render_template_string

📁 Estrutura do Projeto
todo_app_unico_arquivo.py
Tudo (backend + frontend) está dentro de um único arquivo.

🚀 Como rodar o projeto
1️⃣ Criar um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
2️⃣ Instalar o Flask
pip install flask
3️⃣ Executar a aplicação
python todo_app_unico_arquivo.py
4️⃣ Abrir no navegador
http://127.0.0.1:5000
🖥️ Funcionalidades
✅ Adicionar nova tarefa

🔁 Marcar/desmarcar tarefa como concluída

🗑️ Remover tarefa

📊 Exibir total de tarefas

✨ Interface HTML simples e clara

🧩 Principais Rotas
Rota	Método	Descrição
/	GET	Página principal
/add	POST	Adiciona uma tarefa
/toggle/<id>	POST	Conclui / desfaz tarefa
/delete/<id>	POST	Remove tarefa
⚠️ Limitações (intencionais para fins didáticos)
❌ Não usa banco de dados

❌ Não possui autenticação

❌ Não possui proteção CSRF

❌ Dados não persistem

⚠️ Não recomendado para produção

📚 Próximos Passos (Sugestões para Aula)
Persistir dados com SQLite

Separar HTML em templates

Adicionar Flask-WTF (CSRF)

Criar API REST

Usar frontend separado (React, Vue, etc.)

🧑‍🏫 Público-alvo
Iniciantes em Python

Alunos aprendendo backend

Introdução ao Flask

Professores e instrutores

📜 Licença
Este projeto é livre para fins educacionais.

Se quiser, posso:

adaptar esse README para GitHub Classroom

criar slides da aula

evoluir o projeto para Flask + SQLite

transformar em API REST

Só me dizer 👍




Nenhum ficheiro selecionadoNenhum ficheiro selecionado
ChatGPT can make mistakes. Check important info. See Cookie Preferences.
