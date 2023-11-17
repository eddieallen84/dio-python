frutas = ("pera", "laranja", "abacaxi", "morango",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

matriz = (
    (1, "a", 3),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(frutas[0])
print(frutas[1])
print(frutas[-1])
print(frutas[-3])
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

print(frutas.count("morango"))
print(frutas.index("abacaxi"))
print(len(frutas))

