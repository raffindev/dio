from datetime import datetime

class Historico:

    def __init__(self):
        self._transaçoes = []

    def adicionar_transaçao(self, transaçao):
        self._transaçoes.append(transaçao)


class Transaçao:

    def __init__(self, valor=0):
        self._id = 0
        self.data_hora = datetime.now()
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError("O valor da transação deve ser maior que zero.")

    def registro(self):
        return {
            "id": self._id,
            "data/hora": self.data_hora,
            "tipo": "",
            "valor": self._valor,
        }


class Saque(Transaçao):

    def __init__(self, valor):
        super().__init__(valor)

    @property
    def valor(self):
        return self._valor

    def registro(self):
        registro = super().registro()
        registro.update({
            "tipo": "Saque"
        })
        return registro

    def executar(self, conta):
        executar_transaçao = conta.sacar(self.valor)

        if executar_transaçao:
            conta.historico.adicionar_transaçao(self)


class Deposito(Transaçao):

    def __init__(self, valor):
        super().__init__(valor)

    @property
    def valor(self):
        return self._valor

    def registro(self):
        registro = super().registro()
        registro.update({
            "tipo": "Deposito"
        })
        return registro

    def executar(self, conta):
        executar_transaçao = conta.depositar(self.valor)

        if executar_transaçao:
            conta.historico.adicionar_transaçao(self)

