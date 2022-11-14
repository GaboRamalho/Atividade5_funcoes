# Escreva um programa que solicite ao usuário o número de horas
# trabalhadas e a taxa por hora para calcular o salário bruto. Leve em conta
# que a fábrica paga ao funcionário 1,5 vezes a taxa horária para horas
# trabalhadas acima de 40 horas.

def calcula_salario():
    horas_trabalhadas = int(input("Insira quantas horas você trabalhou em valor inteiro: "))
    taxa_hora = float(input("Insira o valor da sua hora em R$: "))

    if horas_trabalhadas > 40: #declara como será calculado em casos de horas extras 
        valor_base = 40 * taxa_hora
        valor_hora_extra = (horas_trabalhadas - 40) * taxa_hora * 1.5
        valor_total_com_extra = valor_base + valor_hora_extra  
        print(f"O seu total a receber é R$ {valor_total_com_extra}")
    
    elif horas_trabalhadas <= 40: #quando não há hora extra, esse é o calculo
        total_trabalhado = horas_trabalhadas * taxa_hora
        print(f"O seu total a receber é R$ {total_trabalhado}")

calcula_salario() #fim