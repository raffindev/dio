# Sistema de Caixa Eletrônico.

menu = """
[1] - Sacar
[2] - Depositar
[3] - Extrato
[0] - Sair
"""

# Variaveis e condicionais.
saldo = 0
numero_saques = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3

# Programa principal
while True:
    print('=' * 5, 'CAIXA ELETRÔNICO', '=' * 5)
    print(menu)

    opção = int(input('Opção desejada: '))
    if opção not in (0, 1, 2, 3):
        print('Opção inválida.')
        continue

    if opção == 1:
        if numero_saques >= LIMITE_SAQUES:
            print('Limite de saque diário atingido')
            continue

        saque = float(input("Digite o valor que gostaria de saque: R$ "))

        if saque <= 0:
            print("Valor inválido")

        elif saque > saldo:
            print("Saque inválido. Saldo insuficiente")
            print(f'Seu saldo é de {saldo:.2f}')

        elif saque > limite:
            print(f'Limite de saque de R$ {limite:.2f}')

        else:
            saldo -= saque
            numero_saques += 1
            extrato += f'Saque R$: {saque:.2f}\n'

            print("Saque realizado com sucesso!")
            print(f"Seu saldo é de R$ {saldo:.2f}")

    elif opção == 2:
        deposito = float(input("Valor que gostaria de depositar: R$ "))

        if deposito <= 0:
            print("Valor inválido")
            continue

        saldo += deposito
        extrato += f'Deposito R$: {deposito:.2f}\n'

        print(f"Depósito realizado com sucesso: R$ {deposito:.2f}.") 
        print(f"Seu saldo é de R$ {saldo:.2f}.")

    elif opção == 3:
        print('-'*5, 'EXTRATO BANCÁRIO', '-'*5)
        print(f'Saldo: R$ {saldo:.2f}')
        print('-'*30)

        if not extrato:
            print('Nenhuma operação realizada hoje.')
        else:
            print(extrato)


    elif opção == 0:
        print('Encerrando...\n')
        break