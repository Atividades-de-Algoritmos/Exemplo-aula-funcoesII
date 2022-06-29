#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 29/06/2022
#
# 1 -  Escreva uma função (que faça uso do while) que recebe um parâmetros e imprime o fatorial.
# teste a função.

################   sem funcao  #########################
numero = int(input('Digite um número inteiro positivo: ')) # Recebe o número do usuário

fat = 1 # inicializa o fatorial com 1 e decrementa o número até chegar a 0
while numero > 0: # enquanto o número for maior que 0 faça o loop abaixo
  fat = fat * numero # multiplica o fatorial pelo número atual e decrementa o número atual em 1
  numero = numero - 1 # decrementa o número atual em 1

print(f'O fatorial desse número é {fat}')


################  com função   ######################
def fat(numero): # função que recebe um número e retorna o fatorial dele
  fat = 1 # inicializa o fatorial com 1 e decrementa o número até chegar a 0
  while numero > 0: # enquanto o número for maior que 0 faça o loop abaixo
    fat = fat * numero # multiplica o fatorial pelo número atual e decrementa o número atual em 1
    numero = numero - 1 # decrementa o número atual em 1
  return fat # retorna o fatorial do número passado por parâmetro



n = int(input('Digite um número inteiro positivo: ')) # Recebe o número do usuário
print(f'O fatorial desse número é {fat(n)}') # chama a função fat e imprime o fatorial do número passado por parâmetro
