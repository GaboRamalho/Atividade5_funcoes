# Crie uma função que itere a lista de números fornecida e imprima apenas
# os números que são divisíveis por 5 (resto = 0).

recebenum = []

def iteranum():
    for c in range (10):
        recebenum.append(
            int(input("Insira um número inteiro: "))
        )

    print(f"Os números inseridos foram {recebenum}")

    if (recebenum % 5 == 0):
        print("Os números divisiveis por 5 são: {recebenum}")
    else:
        print("Os outros números em questão não são divisíveis por 5")

iteranum()
