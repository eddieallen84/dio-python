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
    option = input(menu)
    if option == "d":
        valor = float(input("Valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print("Operação falhou! O Valor informado é inválido")

    elif option == "s":
        valor = float(input("Valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Operação falhou! Seu saldo é insuficiente")
        elif excedeu_limite:
            print("Operação falhou! O valor excedeu o limite por saque")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque de: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif option == "e":
        print("\n============= Extrato =============")
        print('Não foram realizadas movimentações' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f} ')
        print('===================================')

    elif option == "q":
        break

    else:
        print("Opção inválida, por favor selecione uma opção válida")

