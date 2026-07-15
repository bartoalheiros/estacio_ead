class Conta_:
    def __init__(self, clientes, numero, cpf, nomeTitular, saldo):
        self.clientes = clientes
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente"
        else:
            self.saldo -= valor
            return "Transferência Realizada!"

    def gerar_saldo(self):
        print(f"numero: {self.numero} \nsaldo: {self.saldo}")

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente"
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return "Transferência Realizada"

def main():
    c1 = Conta_(1, 1, "Joao", 0)  # Objeto sendo criado
    c1.depositar(300)
    saque = c1.sacar(400)
    c1.gerar_saldo()
    print(f"O saque foi realizado? {saque}")

if __name__ == "__main__":
    main()