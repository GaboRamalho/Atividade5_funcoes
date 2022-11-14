# Crie uma função com um argumento (escolha qualquer nome de
# argumento que desejar). Se o tipo do argumento for int ou float, a função
# deve retornar o valor absoluto da entrada da função. Caso contrário, a
# função deve retornar "Valor informado não é um número";. Verifique se
# funciona chamando a função com -5.6 e Uma string.

#inicio da função
def recebearg(x): 
    if type(x) == int:
        print(abs(x)) #abs() é para colocar o número em módulo
    
    elif type(x) == float:
        print(abs(x))

    else:
        print("Valor informado não é um número.")

recebearg("Abigail")  #fim