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

# HTML único (template). Usamos Jinja2 no próprio arquivo.
HTML_TEMPLATE = """
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <title>Todo App Simples</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 2rem; }
    .done { text-decoration: line-through; color: gray; }
    .todo { margin: 0.5rem 0; padding: 0.5rem; border: 1px solid #eee; border-radius: 4px; }
    form { margin-bottom: 1rem; }
    button { margin-left: 0.5rem; }
  </style>
</head>
<body>
  <h1>Lista de Tarefas (TODO)</h1>

  <!-- Formulário para adicionar novo TODO -->
  <form method="post" action="{{ url_for('add') }}">
    <input type="text" name="text" placeholder="Nova tarefa" required>
    <button type="submit">Adicionar</button>
  </form>

  <!-- Mostrar quantidade e lista -->
  <p>Total: {{ todos|length }} tarefa(s)</p>

  {% if todos %}
    <div>
      {% for t in todos %}
        <div class="todo">
          <strong>#{{ t.id }}</strong>
          <span class="{{ 'done' if t.done else '' }}">{{ t.text }}</span>

          <!-- Form para marcar/desmarcar como feita -->
          <form style="display:inline" method="post" action="{{ url_for('toggle', todo_id=t.id) }}">
            <button type="submit">{{ 'Desfazer' if t.done else 'Concluir' }}</button>
          </form>

          <!-- Form para remover -->
          <form style="display:inline" method="post" action="{{ url_for('delete', todo_id=t.id) }}">
            <button type="submit">Remover</button>
          </form>
        </div>
      {% endfor %}
    </div>
  {% else %}
    <p>Nenhuma tarefa. Adicione a primeira!</p>
  {% endif %}

  <hr>
  <p><small>Dados mantidos em memória — reiniciar o servidor limpa a lista.</small></p>
</body>
</html>
"""
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
