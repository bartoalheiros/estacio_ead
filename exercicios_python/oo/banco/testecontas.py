from Conta_ import Conta_
from Cliente import Cliente

def main():
    cliente1 = Cliente("123", "Joao", "Rua X")
    cliente2 = Cliente("456", "Maria", "Rua W")
    conta1 = Conta_([cliente1, cliente2], 1, 2000)
    conta1.depositar(1000)
    conta1.sacar(1500)
    conta1.extrato.extrato(conta1.numero)

if __name__ == "__main__":
    main()