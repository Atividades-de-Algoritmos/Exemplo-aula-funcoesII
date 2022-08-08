#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 08/08/2022
#
# 2-  Escreva uma função que recebe um número n (inteiro) como parâmetro e imprime a sequencia de Fibonacci ate esse número, teste a função. 

# Link apoio: https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci


# -- Definindo funções --

def fibonacci(n): # função que recebe um número e retorna a sequência de Fibonacci até esse número
  
  a = 0 # Inicializa a como 0
  
  b = 1 # Inicializa b como 0
  
  contador = 2 # E começa a contagem já do 2, porque os dois primeiros números da sequência são esses mesmos.
  
  print(a, b, end = ' ') # Print nos dois valores, end=' ' para não quebrar de linha do próximo elemento

  while contador <= n: # Enquanto o contador for menor que n, faça o loop abaixo
    
    novo_valor = a + b # O novo valor da sequência é sempre a soma do dos último dois valores
    
    print(novo_valor, end = ' ') # Imprimindo o novo valor, end = ' ' para não quebrar linha do próximo elemento
    
    a = b # O primeiro valor agora passa a ser o último
    
    b = novo_valor # E novo valor que acabou de ser mostrado passa a ser nosso último elemento
    
    contador += 1 # Incrementando mais um ao contador para ter a nossa condição de parada

n = int(input('Informe um número para a sequência de Fibonacci: ')) # Recebe o número do usuário

fibonacci(n) # Chama a função fibonacci e imprime a sequência de Fibonacci até o número passado por parâmetro

print('\n\nFim do programa ') # Informando ao usuário que o programa terminou