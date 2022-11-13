# Crie uma função que itere a lista de números fornecida e imprima apenas
# os números que são divisíveis por 5 (resto = 0).

#declaração das listas 
recebenum = []

#função para iterar os números na lista 
def iteranum():
    for c in range (10):
        recebenum.append(
            int(input("Insira um número inteiro: ")) 
        )

    print(f"Os números inseridos foram {recebenum}")    

    for c in recebenum: #estrutura para percorrer a lista e identificar a divisão por 5
        if ( c % 5 == 0):
            print(f"Os números divisiveis por 5 são: {c}")

    for i in recebenum: #estrutura para percorrer a lista e identificar os NÃO divisiveis 5
        if ( i % 5 != 0):
            print(f"Os números NÃO divisiveis por 5 são: {i}") 

iteranum()#fim
