carros = set(['palio', 'uno', 'gol', 'celta', 'palio', 'fox', 'fox'])
fruta = set("abacaxi")
linguagens = {"python", "java", "python", "c"}


numeros = {2, 3, 2, 4}

print(carros)
print(sorted(fruta))
print(linguagens)
print(numeros)

numeros = list(numeros)
print(numeros)
print(numeros[1])

for carro in carros:
    print(carro, end=" ")

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

conjunto_a = {1, 2}
conjunto_b = {3, 4}
conjunto_c = conjunto_a.union(conjunto_b)
print(conjunto_c)

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_c = (conjunto_a.intersection(conjunto_b))
print(conjunto_c)

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_c = (conjunto_a.difference(conjunto_b), conjunto_b.difference(conjunto_a))
print(conjunto_c)

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}
print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

conjunto = {1, 2, 3}
print(conjunto)
conjunto.add(4)
print(conjunto)
conjunto.copy()
print(conjunto)
conjunto.discard(2)
print(conjunto)
conjunto.pop()
print(conjunto)
conjunto.remove(4)
print(conjunto)
print(1 in conjunto)
print(3 in conjunto)
conjunto.clear()
print(conjunto)
