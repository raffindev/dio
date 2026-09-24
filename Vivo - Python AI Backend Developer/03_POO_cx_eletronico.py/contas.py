from transaçao import Historico

class Conta:

    def __init__(self, cliente, numero_conta):
        self._cliente = cliente
        self.agencia = "0001"
        self.numero = numero_conta
        self._saldo = 0
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido: Valor do saque deve ser maior que zero.")

        elif valor > self._saldo:
            print("Saldo insuficiente: Saque não realizado.")

        else:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True

        return False

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido: Valor do depósito deve ser maior que zero.")
            return False
        else:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
            return True


class ContaCorrente(Conta):

    def __init__(self, cliente, numero_conta, limite=500, limite_saques=3):
        super().__init__(cliente, numero_conta)
        self.limite = limite
        self.limite_saques = limite_saques
        self._saques_realizados = 0

    def sacar(self, valor):

        if self._saques_realizados >= self.limite_saques:
            print("Limite de saques atingido.")
            return False

        if valor > self.limite:
            print("Valor de saque excedeu o limite.")
            return False

        saque_realizado = super().sacar(valor)
        if saque_realizado:
            self._saques_realizados += 1
            return True

        return False