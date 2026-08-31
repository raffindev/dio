# Funções relacionadas ao caixa eletrônico

import json
from pathlib import Path
from usuario import buscar_usuario, criar_usuario

# Iniciar caixa
def iniciar_caixa(diretorio):
    diretorio = Path(diretorio)

    with open(diretorio / "usuario.json", "r", encoding="utf-8") as arquivo_usuario:
        lista_usuarios = json.load(arquivo_usuario)

    with open(diretorio / "contas.json", "r", encoding="utf-8") as arquivo_contas:
        lista_contas = json.load(arquivo_contas)

    print("=" * 30)
    print("Iniciar Caixa Eletrônico")
    print("=" * 30)

    cpf = input("\nLogin [CPF]: ").replace(".", "").replace("-", "")

    if len(cpf) != 11 or not cpf.isnumeric():
        print("CPF inválido")
        return

    usuario = buscar_usuario(lista_usuarios, cpf)

    if usuario is None:
        usuario = criar_usuario(lista_usuarios, diretorio)

    return usuario, lista_usuarios, lista_contas

# Sacar
def sacar(*, saldo, extrato, limite_valor_saque, numero_saques, limite_saques):

    if numero_saques >= limite_saques:
        print("Limite de saque diário atingido")
        return saldo, extrato, numero_saques

    saque = float(input("Digite o valor que gostaria de saque: R$ "))

    if saque <= 0:
        print("Valor inválido")

    elif saque > saldo:
        print("Saque inválido. Saldo insuficiente")
        print(f"Seu saldo é de {saldo:.2f}")

    elif saque > limite_valor_saque:
        print(f"Limite de saque de R$ {limite_valor_saque:.2f}")

    else:
        saldo -= saque
        numero_saques += 1
        extrato.append(f"Saque: R$ {saque:.2f}")

        print("Saque realizado com sucesso!")
        print(f"Seu saldo é de R$ {saldo:.2f}")

    return saldo, extrato, numero_saques

# Depositar
def depositar(saldo, extrato, /):
    while True:
        deposito = float(input("Valor que gostaria de depositar: R$ "))

        if deposito <= 0:
            print("Valor inválido")
            continue

        saldo += deposito
        extrato.append(f"Depósito: R$ {deposito:.2f}")

        print(f"Depósito realizado com sucesso: R$ {deposito:.2f}.") 
        print(f"Seu saldo é de R$ {saldo:.2f}.")

        return saldo, extrato

# Exibir Extrato
def exibir_extrato(saldo, /, *, extrato):
    print("-" * 5, "EXTRATO BANCÁRIO", "-" * 5)
    print(f"Saldo: R$ {saldo:.2f}")
    print("-" * 30)

    if not extrato:
        print("Nenhuma operação realizada hoje.")

    else:
        for i, operacao in enumerate(extrato, start=1):
            print(f"{i}. {operacao}")

# menu Cx Eletrônico
def menu_caixa_eletronico(conta, lista_contas, diretorio):
    diretorio = Path(diretorio)

    print("=" * 30, "CAIXA ELETRÔNICO", "=" * 30, "\n")

    saldo = conta["saldo"]
    numero_saques = 0
    limite_valor_saque = 500
    LIMITE_SAQUES = 3
    extrato = []

    while True:

        print("""
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
""")

        menu_caixa = int(input("Digite uma opção: "))

        if menu_caixa not in (1, 2, 3, 0):
            print("Opção inválida.")
            continue

        if menu_caixa == 1:
            saldo, extrato = depositar(saldo, extrato)

        elif menu_caixa == 2:
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                limite_valor_saque=limite_valor_saque,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif menu_caixa == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif menu_caixa == 0:

            conta["saldo"] = saldo

            with open(diretorio / "contas.json", "w", encoding="utf-8") as arquivo:
                json.dump(lista_contas, arquivo, indent=4, ensure_ascii=False)

            print("Encerrando...")
            break