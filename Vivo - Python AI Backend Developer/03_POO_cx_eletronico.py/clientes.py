class Cliente:

    def __init__(self, pessoa):
        self.dados = {}
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if conta in self.contas:
            transacao.executar(conta)   

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):

    def __init__(self, nome, ano_nascimento, cpf, telefone, endereço):
        super().__init__()

        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.cpf = cpf
        self.telefone = telefone
        self.endereço = endereço
        self.dados = self.registro()

    def registro(self):
        return {
            "nome": self.nome,
            "ano_nascimento": self.ano_nascimento,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "endereço": self.endereço
        }