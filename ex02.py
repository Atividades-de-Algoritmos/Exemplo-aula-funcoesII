#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 29/06/2022
#
# 2-  Escreva uma função que recebe um número n (inteiro) como parâmetro e imprime a sequencia de Fibonacci ate esse número, teste a função. https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci
#
# sem função
n = int(input('infrome um número para a sequência de Fibonacci: ')) # Recebe o número do usuário

a, b = 0, 1 # inicializa a e b com 0 e 1 e decrementa a até chegar ao número passado por parâmetro e imprime a sequência de Fibonacci
while a < n: # enquanto a for menor que n faça o loop abaixo (a é o número atual e b é o número anterior)
    print(a, end=',') # imprime a atual e decrementa a em 1 e atualiza b para a atual + b anterior
    a, b = b, a + b # atualiza a e b para a atual + b anterior e decrementa b em 1
print('\u26C4','FIM') # \u26C4 -> boneco de neve



##### com função
def fib(n): # função que recebe um número e retorna a sequência de Fibonacci até esse número
  a, b = 0, 1 # inicializa a e b com 0 e 1 e decrementa a até chegar ao número passado por parâmetro e imprime a sequência de Fibonacci
  while a < n: # enquanto a for menor que n faça o loop abaixo (a é o número atual e b é o número anterior)
      print(a, end=',') # imprime a atual e decrementa a em 1 e atualiza b para a atual + b anterior
      a, b = b, a + b # atualiza a e b para a atual + b anterior e decrementa b em 1
  return '\u26C4','FIM' # \u26C4 -> boneco de neve

n = int(input('infrome um número para a sequência de Fibonacci: ')) # Recebe o número do usuário
print(fib(n)) # chama a função fib e imprime a sequência de Fibonacci até o número passado por parâmetro




