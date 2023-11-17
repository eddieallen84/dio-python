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
