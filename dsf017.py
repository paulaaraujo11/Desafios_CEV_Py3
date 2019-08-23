from math import hypot
print('=======Desafio 017=========\n')
co = float(input('Comprimento do cateto oposto:' ))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co,ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))
