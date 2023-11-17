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
print(matriz[0][1])

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(pares)
print(impares)

pares1 = [numero for numero in numeros if numero % 2 == 0]
print(pares1)

quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

