v_casa = int(input())
v_salario = float(input())
n_anos = int(input())

v_mensal = v_casa/(n_anos*12)

if v_mensal > (v_salario*0.3):
	print('Vai dar não viu lindah... :/')
else:
	print('Negociação aprovada!')