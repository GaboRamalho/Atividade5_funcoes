# A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes,
# coletando dados sobre o salário e número de filhos. Leia esses dados para
# um número não determinado de pessoas e retorne por meio de uma
# função a média de salário da população, a média do número de filhos, o
# maior salário e o percentual de pessoas com salário até 3 salários mínimos
# (~R$ 1.200).


def main ():
   media_salario = []
   media_filhos = []

   getIntput(media_salario, media_filhos)
   
   print(f"A média salarial é igual a: {getMediaSalario(media_salario)}")
   print(f"A média de filhos é igual a: {getMediaFilhos(media_filhos)}")
   print(f"O maior salário é igual a R$ {getMaxSalario(media_salario)}")
   print(f"A quantidade de pessoas com salário inferior a 3 salários minimos é igual a: {getPercentual(media_salario, media_filhos)}%")



def getIntput(media_salario, media_filhos):
   while True: #estrutura de repetição para resgatar valor de salário e quantidade de filhos
      continua = int(input("Gostaria de inserir algum dado?: (1) Sim (2) Nao\n"))

      if continua == 2:
         break
      elif continua == 1:
         user_input_salario = float(input("Insira seu salário: R$ "))
         user_input_filho = int(input("Insira a quantidade de filhos ou dependentes menor que 21 anos você possui: "))
         media_salario.append(user_input_salario)
         media_filhos.append(user_input_filho)

      else: 
         print("Numero invalido")

def getMediaSalario(media_salario):
    num = sum(media_salario)
    total = len(media_salario)
    
    return num/total

def getMediaFilhos(media_filhos):
    num = sum(media_filhos)
    total = len(media_filhos)
    
    return num/total

def getMaxSalario(media_salario):
    total = max(media_salario)

    return total

def getPercentual(media_salario, media_filhos):
    salario_minimo = (media_salario)
    quantidadePessoas = len(media_filhos)

    if salario_minimo <= 3600:
        porcentagem = (salario_minimo / float(quantidadePessoas)) * 100


    return porcentagem

main()