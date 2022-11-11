# Defina uma função calcularCubo() que recebe um argumento tipo inteiro.
# Faça essa função retornar o cubo desse número (ou seja, elevado a 3).
# Defina uma segunda função que recebe um argumento tipo inteiro. Se
# esse número for divisível por 3, a segunda função deve chamar
# calcularCubo() e retornar seu resultado. Caso contrário, a segunda função
# deve retornar uma mensagem.

#função para calcular cubo
def calcular_cubo(a):
    numero_cubico= a
    cubo = numero_cubico ** 3 
    return f"o cubo de {numero_cubico} é igual a {cubo:.2f}\n"

#função para testar divisão por 3
def divtres():

    numero_div = int(input("Insira um número inteiro: "))
    if (numero_div % 3 == 0):
        return (calcular_cubo(numero_div))
    else:
        print(f"{numero_div} não é divisível por três")

print(divtres())
