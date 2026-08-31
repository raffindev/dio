# Funções relacionadas a usúario e conta
import json
from datetime import date

# Criar usuário
def criar_usuario(lista_usuarios, diretorio):
    print("=" * 30)
    print("Cadastrar Usuário".center(30))
    print("=" * 30)
    while True:
            cpf = input('\nDigite seu CPF: ').replace('.','').replace('-','')
    
            if len(cpf) != 11 or not cpf.isnumeric():
                print("CPF inválido")
    
            elif any(cpf == usuario["cpf"] for usuario in lista_usuarios):
                print('CPF já cadastrado.')
                
            else:
                break
            

    nome = input("Digite seu nome completo: ").strip()

    print("A seguir sua data de nascimento:")
    while True:
        try:
            dia = int(input("Dia: "))
            mes = int(input("Mês: "))
            ano = int(input("Ano: "))

            hoje = date.today()

            data_nascimento = date(ano, mes, dia)
            if data_nascimento > hoje:
                print("A data de nascimento não pode ser futura.")
            else:
                break

        except ValueError:
            print("Somente números válidos devem ser informados.")
    
    while True:

        endereço_logradouro = input("logradouro: ").strip()
        if not endereço_logradouro:
            print("Logradouro não pode ficar vazio")
            continue

        endereço_numero = input("número: ").strip()

        endereço_bairro = input("bairro: ").strip()
        if not endereço_bairro:
            print("Bairro não pode ficar vazio")
            continue

        endereço_cidade = input("informe a cidade: ")
        endereço_estado = input("informe a sigla do estado: ")
        break

    usuario = {
        "nome": nome,
        "data_nascimento": str(data_nascimento),
        "cpf": cpf,
        "endereço": {
            "logradouro": endereço_logradouro,
            "numero": endereço_numero,
            "bairro": endereço_bairro,
            "cidade": endereço_cidade,
            "estado": endereço_estado
        }
    }

    lista_usuarios.append(usuario)

    with open(diretorio / "usuario.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista_usuarios, arquivo, indent=4, ensure_ascii=False)

    return usuario
    

def buscar_usuario(lista_usuarios, cpf):
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            return usuario

    return None