km = int(input('Quantos km vc vai viajar: '))
if (km > 200):
	preco = km * 0.45
else:
	preco = km * 0.5
print(f'O valor da viagem ficou por {preco}!')
