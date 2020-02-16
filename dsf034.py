salario = float(input('Qual o valor do seu salário? ')) 
if (salario > 1250.00):
	aumento = salario * 0.1
else:
	aumento = salario * 0.15
print(f'Seu aumento será de {aumento:.2f}')