# Faça uma função que computa a potência a b para valores a e b (assuma
# números inteiros) passados por parâmetro (não use o operador **).


#função para receber base e expoente
def potencia():
    base = int(input("Insira a base: ")) #base a
    expoente = int(input("Insira o expoente: ")) #expoente b
    resultado = 1

 # para calcular: base^expoente = base * base (expoente vezes)   
    for numero in range(1, expoente+1):
        resultado = resultado * base
    print(f"{base} elevado a {expoente} é igual a: {resultado}")

potencia() #fim