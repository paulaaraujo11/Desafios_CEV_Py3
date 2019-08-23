print('============Desafio 015==============')

d = int(input('Quanto(s) dia(s) alugados?'))
km = float(input('Quantos Km rodado(s)?'))
preco = d*60 + km*0.15
print('O total a pagar é de R${:.2f}'.format(preco))
