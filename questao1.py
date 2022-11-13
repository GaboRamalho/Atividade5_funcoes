# Use uma função que receba um valor n inteiro e imprima até a n-ésima
# linha para um n informado pelo usuário.


#inicio da função
def nlinhas(n):
    for i in range(n): #condição para a quantidade de linhas e colunas 
        i += 1
        print(str(i) * i)

n = int(input('Insina um número inteiro e eu imprimirei a mesma quantidade de linha e sequência: '))
nlinhas(n)#fim