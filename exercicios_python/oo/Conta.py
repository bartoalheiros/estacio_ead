#construtores e metodo init e self
# self é a forma da classe se referir a ela mesma
# --init-- é o mo metodo construtor que cria o objeto da classe
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def gerar_extrato(self):
        print(f"numero: {self.numero} \n cpf: {self.cpf}\nsaldo: {self.saldo}")

def main():
    c1 = Conta(1, 1, "Joao", 0) # Objeto sendo criado
    c1.depositar(300)
    c1.gerar_extrato()
    c1.sacar(100)
    c1.gerar_extrato()

if __name__ == "__main__":
    main()