from datetime import date

data_atual = date.today().year
data_nasc = int(input('Ano do seu nascimento: '))
idade = data_atual - data_nasc
print(f'Quem nasceu em {data_nasc} tem {idade} anos em {data_atual}')
if idade == 18:
	print('Você tem que se alistar imediatamente!')
else:
	if idade < 18:
		print(f'Ainda faltam {18-idade} anos para seu alistamento!')
	else:
		print(f'Você já devia ter se alistado há {idade-18} anos!')