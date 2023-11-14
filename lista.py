numeros = list((range(10)))
letras = list("python")
frutas = ["maçã", "pera", "uva", "abacate"]
matriz = [
    [1, "a", 3],
    ["b", 3, 4],
    [6, 5, "c"]
]
carros = ["gol", "celta", "uno"]

print(numeros)

print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

print(frutas[2])
print(matriz[0][0])

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

pares = []
for numero in numeros:
    if numero %2 == 0:
        pares.append(numero)
print(pares)

