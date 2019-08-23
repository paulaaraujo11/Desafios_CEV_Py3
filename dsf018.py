from math import radians,sin,cos,tan
print('=======Desafio 018=========\n')
ang = float(input('Digite o valor do angulo:'))
sin = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))
print('\nPara o ângulo {}\nO seno vale {:.2f}\nO cosseno vale {:.2f}\nE a tangente vale {:.2f}'.format(ang,sin,cos,tg))
