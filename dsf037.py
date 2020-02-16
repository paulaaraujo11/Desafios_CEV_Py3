num = int(input('Digite um número inteiro'))
print('''Escolha uma opção para conversão:
	1 - Binário | 2 - Octal | 3 - Hexadecimal''')
opcao = int(input('Sua opção: '))

if opcao == 1:
	print(f'{num} em binário : {bin(num)[2:]}')
elif opcao == 2:
	print(f'{num} em octal : {oct(num)[2:]}')
elif opcao == 3:
	print(f'{num} em hexadecimal : {hex(num)[2:]}')
else:
	print('Tente novamente')