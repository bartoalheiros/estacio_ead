variavel = 10
def func():
    global variavel
    variavel = 5

func()
print(variavel)