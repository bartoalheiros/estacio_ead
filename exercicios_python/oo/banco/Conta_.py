import datetime
from Extrato import Extrato

class Conta_:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.dataabertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente"
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True

    def get_clientes(self):
        return self.clientes

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente"
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            return "Transferência Realizada"

    def gerasaldo(self):
        print(f"numero: {self.numero} \nsaldo: {self.saldo}")

def main():
    c1 = Conta_(1, 1, 0)
    c1.depositar(300)
    saque = c1.sacar(400)
    c1.gerasaldo()
    print(f"O saque foi realizado? {saque}")

if __name__ == "__main__":
    main()