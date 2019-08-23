print('='*20,'DESAFIO 012','='*20,'\n')

preco = float(input('Digite o valor do produto: '))

novo_preco =  preco - ((preco/100)*5)

print('O novo preço é de R${:.2f}'.format(novo_preco))
