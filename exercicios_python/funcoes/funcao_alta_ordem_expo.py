'''
No próximo exemplo, script potencia.py, implementamos a função superior calcula_potencia. Essa função recebe por parâmetro
um número inteiro que será o expoente da potenciação (linha 2) e tem uma função interna (potencia), cujo argumento será a
base no cálculo de potência a ser realizado por ela (linhas 3 a 5). Para esse exemplo, utilizaremos um emulador de códigos.

Na parte principal do programa, função main (linha 8), recebemos os valores de base e expoente informados pelo usuário do
programa, por meio da função nativa do Python chamada input (linha 9). A seguir, como a função input retorna os valores em
forma de string, separamos esses valores por meio da função nativa split, e os convertemos para inteiros, atribuindo-os às variá-
veis base e expoente, respectivamente (linha 11). Invocamos calcula_potencia, passando o valor do expoente por parâmetro, que
nos retornará uma instância da função potencia que será então atribuída à variável potencia_de (linha 14). Utilizando
potencia_de com o argumento base, invocamos indiretamente a função potencia para efetuar a potenciação propriamente dita,
sendo que o seu retorno será armazenado na variável res_potencia (linha 15). Finalmente, imprimimos no console o resultado fi-
nal (linha 16).
'''

# script potencia.py
def calcula_potencia(expoente):
        def potencia(base):
            return base**expoente
        return potencia

# parte principal do programa
def main():
    base_expoente = input()
    # separa base e expoente,
    # convertendo-os para inteiros
    base, expoente = (int(i) for i in
    base_expoente.split())

    # utilizando a função
    # calcula_potencia
    potencia_de = calcula_potencia(expoente)
    res_potencia = potencia_de(base)

    print(f"{base} elevado a {expoente} = {res_potencia}")

if __name__ == "__main__":
        main()