# Exemplo básico para treinamento em Python: listas, tuplas, conjuntos e dicionários
# Comentários em Português e prints para facilitar o entendimento.
# Compatível com Python 3.x — rode: python treinamento_basico_listas.py

# -----------------------
# 1) Listas (mutable)
# -----------------------

# Listas são coleções ordenadas e mutáveis (podem mudar depois de criadas).
frutas = ["maçã", "banana", "laranja"]
print("Lista original de frutas:", frutas)

# Acessar por índice (começa em 0)
print("Primeira fruta:", frutas[0])

# Fatiamento (slicing)
print("Fatiamento frutas[1:]:", frutas[1:])  # a partir do índice 1 até o fim

# Adicionar elementos
frutas.append("uva")           # adiciona ao final
print("Depois de append('uva'):", frutas)

frutas.insert(1, "morango")    # insere na posição 1
print("Depois de insert(1, 'morango'):", frutas)

# Estender com outra lista
outras = ["abacate", "kiwi"]
frutas.extend(outras)
print("Depois de extend(['abacate','kiwi']):", frutas)

# Remover elementos
frutas.remove("banana")        # remove a primeira ocorrência
print("Depois de remove('banana'):", frutas)

removido = frutas.pop()        # remove e retorna o último elemento
print("Elemento removido por pop():", removido)
print("Lista agora:", frutas)

# Limpar a lista
# frutas.clear()
# print("Depois de clear():", frutas)

# Iterar sobre lista
print("Iterando sobre frutas:")
for f in frutas:
    print(" -", f)

# Métodos úteis
print("Quantidade de elementos (len):", len(frutas))
print("Apareceu 'maçã'?", "maçã" in frutas)

# Cópia (shallow copy)
copia_frutas = frutas.copy()
print("Cópia das frutas:", copia_frutas)

# Ordenar (in-place) e criar versão ordenada sem alterar original
nums = [5, 2, 9, 1]
print("nums original:", nums)
nums.sort()                   # modifica a lista original
print("nums ordenado (sort):", nums)
nums2 = sorted([3, 7, 0])     # retorna nova lista ordenada
print("sorted([3,7,0]):", nums2)

# List comprehension (forma compacta de criar listas)
quadrados = [x*x for x in range(6)]
print("Quadrados (list comprehension):", quadrados)

# -----------------------
# 2) Tuplas (immutable)
# -----------------------
# Tuplas são parecidas com listas, mas imutáveis (não podem ser alteradas depois de criadas).
coordenadas = (10.0, 20.0)
print("\nTupla coordenadas:", coordenadas)
print("Primeiro valor da tupla:", coordenadas[0])

# Tuplas podem ser usadas para retornar múltiplos valores
def divisao_resto(a, b):
    return a // b, a % b  # retorna uma tupla (quociente, resto)

q, r = divisao_resto(7, 3)  # desempacotamento de tupla
print("Divisão 7//3 =", q, "resto =", r)

# Tentar alterar a tupla causa erro (descomente para testar)
# coordenadas[0] = 5.0  # TypeError: 'tuple' object does not support item assignment

# Converter entre tupla e lista
lista_de_coordenadas = list(coordenadas)
lista_de_coordenadas.append(30.0)
nova_tupla = tuple(lista_de_coordenadas)
print("Converter tupla -> lista -> tupla:", nova_tupla)

# -----------------------
# 3) Conjuntos (set)
# -----------------------
# Conjuntos são coleções não ordenadas de elementos únicos.
frutas_misturadas = ["maçã", "banana", "maçã", "laranja"]
conjunto_frutas = set(frutas_misturadas)
print("\nConjunto (elementos únicos):", conjunto_frutas)

# Operações de conjuntos
a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])
print("Interseção (a & b):", a & b)
print("União (a | b):", a | b)
print("Diferença (a - b):", a - b)

# Adicionar e remover
a.add(10)
a.discard(2)  # discard não levanta erro se o elemento não existir
print("Conjunto a após add e discard:", a)

# -----------------------
# 4) Dicionários (dict)
# -----------------------
# Dicionários armazenam pares chave: valor. Chaves devem ser únicas e imutáveis (ex: strings, tuplas).
pessoa = {
    "nome": "Ana",
    "idade": 30,
    "idiomas": ["Português", "Inglês"]
}
print("\nDicionário pessoa:", pessoa)

# Acessar valor pela chave
print("Nome:", pessoa["nome"])
# Usar get para evitar KeyError quando a chave não existir
print("Profissão (get):", pessoa.get("profissao", "não informada"))

# Inserir / atualizar
pessoa["idade"] = 31  # atualiza
pessoa["cidade"] = "São Paulo"  # adiciona nova chave
print("Dicionário atualizado:", pessoa)

# Iterar sobre chaves, valores e itens (par chave-valor)
print("Iterando chaves:")
for chave in pessoa:
    print("-", chave)

print("Iterando itens (chave, valor):")
for chave, valor in pessoa.items():
    print(chave, "=", valor)

# Remover item
idade = pessoa.pop("idade")
print("idade removida com pop:", idade)
print("pessoa agora:", pessoa)

# -----------------------
# 5) Estruturas aninhadas
# -----------------------
# Listas com listas, dicionários com listas etc.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
]
print("\nMatriz (lista de listas):", matriz)
print("Elemento linha 1 coluna 2:", matriz[0][1])

agenda = {
    "João": ["1111-1111", "joao@example.com"],
    "Maria": ["2222-2222", "maria@example.com"]
}
print("Agenda:", agenda)
print("Email da Maria:", agenda["Maria"][1])

# -----------------------
# 6) Boas práticas / dicas básicas
# -----------------------
# - Use listas quando precisar de uma sequência ordenada e mutável.
# - Use tuplas quando os dados não devem mudar (e.g., coordenadas, chaves).
# - Use sets quando quiser elementos únicos e operações matemáticas (união/interseção).
# - Use dicts para mapear chaves a valores (e.g., registros).
# - Prefira métodos como .append() e .extend() para adicionar itens em listas.
# - Prefira .get() em dicts quando a chave pode não existir.
# - Atenção à mutabilidade: copiar listas com = cria uma referência; use .copy() para uma cópia rasa.

# Exemplo mostrando referência vs cópia
orig = [1, 2, 3]
ref = orig        # ambos apontam para a mesma lista
cop = orig.copy() # cópia separada
ref.append(4)
print("\norig após modificar ref (mesma referência):", orig)
cop.append(5)
print("cop (cópia separada):", cop)
print("orig final:", orig)

# -----------------------
# 7) Exercícios sugeridos (para praticar)
# -----------------------
# 1) Crie uma lista com 5 números e calcule a média.
# 2) Dado um dicionário com notas de alunos, calcule a média da turma.
# 3) Transforme uma lista com elementos repetidos em uma lista sem repetições (use set).
# 4) Crie uma função que recebe uma lista e retorna os 3 maiores valores (dica: sorted).

print("\nFim do exemplo. Experimente modificar o arquivo e rodar de novo para ver os efeitos.")
