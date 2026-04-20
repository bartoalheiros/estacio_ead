def escopo( ):
    global variavel_a
    variavel_a = 1 # Variável global
    variavel_b = 2 # Variável global
    print("Variável A dentro da função:", variavel_a)
    print("Variável B dentro da função:", variavel_b)
    print("Variável C dentro da função:", variavel_c)

variavel_a = 10 # Variável global
variavel_b = 20 # Variável global
variavel_c = 30 # Variável global

escopo()

print("Variável A global:", variavel_a)
print("Variável B global:", variavel_b)
print("Variável C global:", variavel_c)