# Dados dois números inteiros, retorne seu produto somente se o produto
# for igual ou menor que 1000, caso contrário, retorne sua soma.

def recebedados():
    numero1 = int(input("Insira um número inteiro: "))
    numero2 = int(input("Insira um segundo número inteiro: "))
    soma = numero1 + numero2
    mult = numero1 * numero2

    return numero1, numero2, soma, mult

def calculo():
    numero1, numero2, soma, mult = recebedados()
    
    if (mult <= 1000):
        print(f"O resultado da soma entre {numero1} e {numero2} é igual: {soma}")
    else:
        print(f"O resultado do produto entre {numero1} e {numero2} é igual: {mult}")

calculo()