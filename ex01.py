#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 08/08/2022
#
# 1 -  Escreva uma função (que faça uso do while) que recebe um parâmetros e imprime o fatorial. certifique-se de testar a função.

# -- Definindo função --

def fat(numero): # Função que recebe um número e retorna o fatorial dele
  fat = 1 # Inicializa o fatorial com 1 e decrementa o número até chegar a 0
  
  while numero > 0: # Enquanto o número for maior que 0 faça o loop abaixo
    fat = fat * numero # Multiplica o fatorial pelo número atual e decrementa o número atual em 1
    numero = numero - 1 # Decrementa o número atual em 1
  return fat # Retorna o fatorial do número passado por parâmetro

n = int(input('Digite um número inteiro positivo: ')) # Recebe o número do usuário
print(f'\nO fatorial desse número é {fat(n)}') # chama a função fat e imprime o fatorial do número passado por parâmetro


# -- Versão 2.0 código By Carlos --

def calcula_fatorial(valor : int): # Função calcula fatorial recebe um valor como parâmetro
  fatorial = 1 # Criando a variável fatorial para fazer alterações nela

  for i in range(valor, 0, -1): # Estrutura de repetição que percorre até chegar no 0
    fatorial *= i # Multiplicando pelo valor anterior
  
  return fatorial # Retornando o valor total do fatorial

print(f'Fatorial {n}! = {calcula_fatorial(n)}') # Chamando a função calcula fatorial e imprimindo o fatorial do número passado no parâmetro