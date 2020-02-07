#desafio 029

velocidade = float(input('Qual sua velocidade atual? '))
if (velocidade>80):
  multa = (velocidade-80)*7
  print(f'Você execedeu o limete de 80km/h, está multádo em R${(multa)}')
print('Dirija com segurança!')