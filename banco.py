menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

==> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito de: R$ {valor:.2f}\n'
        else:
            print("Operação falhou! O Valor informado é inválido")

    elif opcao == "s":
        saque = float(input("Valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Operação falhou! Seu saldo é insuficiente")
        elif excedeu_limite:
            print("Operação falhou! O valor excedeu o limite por saque")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido")

    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione uma opção válida")



