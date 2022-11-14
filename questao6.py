# Dados dois números inteiros, retorne seu produto somente se o produto
# for igual ou menor que 1000, caso contrário, retorne sua soma.


#inicio da função
def recebedados(): #para receber os dados e declarar variáveis
    numero1 = int(input("Insira um número inteiro: "))
    numero2 = int(input("Insira um segundo número inteiro: "))
    soma = numero1 + numero2
    mult = numero1 * numero2

    return numero1, numero2, soma, mult #o que eu desejo retorna da função

def calculo():
    numero1, numero2, soma, mult = recebedados() #chamando as variáveis da 1ª função 
    
    if (mult <= 1000): #condições para saber como printar 
        print(f"O resultado da soma entre {numero1} e {numero2} é igual: {soma}")
    else:
        print(f"O resultado do produto entre {numero1} e {numero2} é igual: {mult}")

calculo() #fim