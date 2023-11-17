pessoa = {"nome": "Eddie", "idade": 39}
pessoa = dict(nome="Eddie", idade=28)
pessoa["telefone"] = "99277-3484"

print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['telefone'])

pessoa['nome'] = "Marcelle"
pessoa['idade'] = 33
pessoa['telefone'] = "99257-1795"

print(pessoa)

contatos = {
    "eddie.xd@gmail.com": {"nome": "Eddie", "telefone": "3333-2121"},
    "joaosilva@outlook.com": {"nome": "João", "telefone": "2234-3232"},
    "lucassilvaesilva@hotmail.com": {"nome": "Lucas", "telefone": "3321-8721", "extra": {"a":1}},
    "mariacp@gmail.com": {"nome": "Maria", "telefone": "3218-3328"},
}

print(contatos["mariacp@gmail.com"]["telefone"])

extra = contatos['lucassilvaesilva@hotmail.com']['extra']
print(extra)

extra = contatos['lucassilvaesilva@hotmail.com']['extra']['a']
print(extra)

for key, valor in contatos.items():
    print(key ,valor)