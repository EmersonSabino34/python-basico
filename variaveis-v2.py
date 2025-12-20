# Exemplo básico de Python com tipos e comentários detalhados

# Tipos básicos
nome: str = "Maria"               # string (texto)
idade: int = 25                   # inteiro
altura: float = 1.68              # número decimal
is_estudante: bool = True         # valor booleano (verdadeiro/falso)






print(f"Nome: {nome} (tipo: {type(nome)})")
print(f"Idade: {idade} (tipo: {type(idade)})")
print(f"Altura: {altura} (tipo: {type(altura)})")
print(f"É estudante? {is_estudante} (tipo: {type(is_estudante)})\n")

# Listas (sequência ordenada de valores)
notas: list[float] = [8.5, 7.0, 9.3]
print(f"Notas: {notas} (tipo: {type(notas)})")
print(f"Média das notas: {sum(notas) / len(notas):.2f}\n")

# Tupla (sequência imutável)
coordenadas: tuple[float, float] = (23.5, 42.1)
print(f"Coordenadas: {coordenadas} (tipo: {type(coordenadas)})\n")

# Dicionário (pares chave-valor)
pessoa: dict[str, str | int | float | bool] = {
    "nome": nome,
    "idade": idade,
    "altura": altura,
    "estudante": is_estudante
}
print(f"Dicionário pessoa: {pessoa} (tipo: {type(pessoa)})\n")

# Função com tipos definidos
def saudacao(nome: str, idade: int) -> str:
    """Retorna uma saudação personalizada."""
    return f"Olá, {nome}! Você tem {idade} anos."

mensagem: str = saudacao(nome, idade)
print(f"Mensagem da função: {mensagem}\n")

# Condicional
if idade >= 18:
    print(f"{nome} é maior de idade.")
else:
    print(f"{nome} é menor de idade.")

# Loop
print("\nListando notas:")
for i, nota in enumerate(notas, start=1):
    print(f" - Nota {i}: {nota}")
