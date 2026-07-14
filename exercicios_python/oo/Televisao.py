class Televisao:
    def __init__(self, canal_atual, canal_maximo, canal_minimo):
        self.canal_atual = canal_atual
        self.canal_maximo = canal_maximo
        self.canal_minimo = canal_minimo

    def canal_menos(self, canal_atual):
        self.canal_atual = self.canal_atual - 1

    def canal_mais(self, canal_atual):
        self.canal_atual = self.canal_atual + 1

def main():
