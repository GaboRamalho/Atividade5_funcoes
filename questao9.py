# Faça uma função que recebe um valor inteiro e verifica se o valor é par ou
# ímpar. A função deve retornar um valor booleano.

def impar_par():
    numero = int(input("Insira um número inteiro para saber se ele é par:"))

    if numero % 2 == 0:
        resultado = True
    else:
        resultado = False

    print(f"{numero} é número par? {resultado}") 

impar_par() #fim