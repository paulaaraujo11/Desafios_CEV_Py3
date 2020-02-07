#desafio 028
from random import randint
from time import sleep

num_pc = randint(0, 5)

print('-=-'*20)
num_user = int(input('Escolha um número entre 0 e 5, duvido você adivinhar... '))
print('-=-'*20)

print('Processando...')
sleep(3)

if(num_pc == num_user):
  print('Acertou mizeravi!!!')
else:
  print(f'Errooouuu =/, Era {num_pc}')