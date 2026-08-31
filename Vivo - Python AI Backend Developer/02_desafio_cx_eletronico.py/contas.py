# Conta corrente
def criar_conta_corrente(lista_contas, usuario):
    numero_conta = len(lista_contas) + 1

    conta = {
        "cpf": usuario["cpf"],
        "agencia": "0001",
        "conta_corrente": numero_conta,
        "saldo": 0
    }

    lista_contas.append(conta)
    return conta


def buscar_conta_corrente(lista_contas, numero_conta, usuario):

    for conta in lista_contas:

        if (conta["conta_corrente"] == numero_conta and conta["cpf"] == usuario["cpf"]):
            return conta

    return None

def menu_conta_corrente(usuario, lista_contas):
    print("=" * 30, "MENU CONTA CORRENTE", "=" * 30, "\n")
    print(f"Bem-vindo, {usuario['nome']}!\n")

    while True:
        print("""
[1] Criar conta corrente
[2] Acessar conta corrente
[0] Sair
""")
        menu = int(input("Digite uma opção: "))
        if menu not in (1, 2, 0):
            print("Opção inválida.")
            continue

        if menu == 1:
            conta_corrente = criar_conta_corrente(lista_contas, usuario)
            return conta_corrente

        elif menu == 2:

            numero_conta = int(input("Digite o número da conta corrente: "))
            conta_corrente = buscar_conta_corrente(lista_contas, numero_conta, usuario)

            if conta_corrente:
                return conta_corrente

            print("Conta corrente não encontrada.")

        elif menu == 0:
            break
