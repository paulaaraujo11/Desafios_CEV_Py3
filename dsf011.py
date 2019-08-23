print('='*20,'DESAFIO 011','='*20,'\n')

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura
tinta = area / 2

print('Su parede tem area de {} m^2 e você precisa de {} litros de tinta'.format(area,tinta))
