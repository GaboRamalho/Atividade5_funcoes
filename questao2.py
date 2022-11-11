# Escreva um programa para criar uma função usando as seguintes condições:
# ele deve aceitar o nome e o salário do funcionário e exibir ambos.
# Se o salário estiver ausente na chamada de função, atribua o valor padrão 9000 ao salário.


#função para receber os dados do usuário
def recebedados():
    print("Bem vindo ao nosso app!")
    nome_funcionario = input("Qual seu nome?")
    salario_funcionario = float(input("Qual o seu salário em reais? R$"))

    return nome_funcionario, salario_funcionario

def apresentadados():
    nome_funcionario, salario_funcionario = recebedados()
    print(f"Olá {nome_funcionario}, seu salário é igual a: R${salario_funcionario:.2f}")

apresentadados()
