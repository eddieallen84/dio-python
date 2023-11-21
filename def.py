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

def exibir_poema
