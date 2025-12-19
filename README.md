Skip to content
Chat history


You said:
"""
todo_app_unico_arquivo.py

Exemplo bem básico de uma aplicação TODO em um único arquivo usando Flask.
- HTML é embutido no arquivo (render_template_string).
- Os dados ficam em memória (lista Python). Ao reiniciar o servidor, os TODOs são perdidos.
- Ideal para aulas ou protótipos. Para produção, usar banco de dados e proteção CSRF.

Como rodar:
1) Instale Flask (se ainda não tiver): pip install flask
2) Rode: python todo_app_unico_arquivo.py
3) Abra no navegador: http://127.0.0.1:5000
"""

from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Lista em memória para armazenar as tarefas.
# Cada tarefa é um dicionário: {"id": int, "text": str, "done": bool}
todos = []
next_id = 1  # id simples incremental





@app.route("/")
def index():
    # Renderiza a página principal com a lista de todos
    return render_template_string(HTML_TEMPLATE, todos=todos)


@app.route("/add", methods=["POST"])
def add():
    # Adiciona uma nova tarefa (vinda do form)
    global next_id
    text = request.form.get("text", "").strip()
    if text:
        todos.append({"id": next_id, "text": text, "done": False})
        next_id += 1
    return redirect(url_for("index"))


@app.route("/toggle/<int:todo_id>", methods=["POST"])
def toggle(todo_id):
    # Marca ou desmarca a tarefa como feita
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = not t["done"]
            break
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    # Remove a tarefa pelo id
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    # Executa o servidor de desenvolvimento
    app.run(debug=True)

faça um readmd dessa aula de python
ChatGPT said:
Aqui está um README.md bem estruturado e didático para essa aula de Python com Flask, pensado para estudantes iniciantes 👇

📝 Todo App Simples com Flask (Arquivo Único)
Este projeto é um exemplo didático de uma aplicação TODO List desenvolvida em Python usando Flask, totalmente contida em um único arquivo.
Ele é ideal para aulas, workshops e protótipos rápidos, ajudando a entender os conceitos básicos de backend com Flask.

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
