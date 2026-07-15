class Televisao:
    def __init__(self, canal_atual, canal_maximo, canal_minimo):
        self.canal_atual = canal_atual
        self.canal_maximo = canal_maximo
        self.canal_minimo = canal_minimo

    def canal_menos(self):
        if self.canal_atual - 1 < self.canal_minimo:
            self.canal_atual = self.canal_maximo
        else:
            self.canal_atual = self.canal_atual - 1

    def canal_mais(self):
        if self.canal_atual + 1 > self.canal_maximo:
            self.canal_atual = self.canal_minimo
        else:
            self.canal_atual = self.canal_atual + 1

    def mostrar_canal(self):
        print(f"Canal Atual: {self.canal_atual}")

def main():
    t1 = Televisao(100, 100, 1)
    t1.mostrar_canal()
    t1.canal_mais()
    t1.mostrar_canal()
    t1.canal_mais()
    t1.mostrar_canal()

if __name__ == "__main__":
    main()