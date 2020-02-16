nota1 = float(input('Digite a 1° nota:  '))
nota2 = float(input('Digite a 2° nota:  '))

media = (nota1 + nota2) / 2

if media >= 7.00:
	print('Parabéns, você foi aprovado!')
elif 5.0 <= media <= 6.9:
	print('Você está em recuperação!')
else:
	print('Você foi reprovado!')