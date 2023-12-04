def exibir_mensagem():
    print("Olá, mundo")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_2("Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Carlos")

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_total([10, 20, 35]))
print(retorna_antecessor_e_sucessor(19))

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}, {modelo}, {ano}, {placa}")

salvar_carro("Fiat", "uno", "2007", "NHD-3342")
salvar_carro(marca="Fiat", modelo="Uno", ano="2007", placa="NHD-3342")
salvar_carro(**{"marca": "Fiat", "modelo": "Uno", "ano": "2007", "placa": "NHD-3342"})

# (**kwargs) passa o resultado da função como um dicionário
# (*args) passa o resultado da função como uma tupla

def exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

exibir_poema("Sexta feira, 24 de novembro de 2023",
 "** Zen Of Python **",
 "Beautiful is better than ugly.",
 "Explicit is better than implicit.",
 "Simple is better than complex.",
 "Complex is better than complicated.",
 "Flat is better than nested.",
 "Sparse is better than dense.",
 "Readability counts.",
 "Special cases aren't special enough to break the rules.",
 "Although practicality beats purity.",
 "Errors should never pass silently.",
 "Unless explicitly silenced.",
 "In the face of ambiguity, refuse the temptation to guess.",
 "There should be one -- and preferably only one -- obvious way to do it.",
 "Although that way may not be obvious at first unless you're Dutch.",
 "Now is better than never.",
 "Although never is often better than *right* now.",
 "If the implementation is hard to explain, it's a bad idea",
 "If the implementation is easy to explain, it may be a good idea",
 "Namespaces are one honking great idea -- let's do more of those!", autor="Tim Peters", ano="1999")

def somar(a, b):
    return a+b
def subtrair(a, b):
    return a-b
def teste (a, b):
    return a * 2 + b * 3
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é {resultado}")

exibir_resultado(10, 15, somar)
exibir_resultado(20, 5, subtrair)
exibir_resultado(5, 3, teste)

op = somar
print(op(2, 50))


teste 123