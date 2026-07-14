class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def main(self):
        c1 = Conta(1,1,"Joao",1000) # Objeto sendo
        # instanciado
