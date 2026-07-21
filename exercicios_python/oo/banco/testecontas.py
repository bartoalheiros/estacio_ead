from Conta_ import Conta_
from Cliente import Cliente

def main():
    cliente1 = Cliente(123, "Joao", "Rua 1")
    cliente2 = Cliente(345, "Maria", "Rua 2")
    cliente3 = Cliente(678, "Carlos", "Rua 3")
    cliente4 = Cliente(91011, "Joana", "Rua 4")

    conta1 = Conta_([cliente1, cliente2], 1, 0)
    conta2 = Conta_([cliente3, cliente4], 2, 0)

    conta1.gerasaldo()
    conta1.depositar(1500)
    conta1.sacar(500)
    conta1.gerasaldo()

    clientes = conta2.get_clientes()
    for cliente in clientes:
        print(cliente.nome)
        print(cliente.endereco)

if __name__ == "__main__":
    main()