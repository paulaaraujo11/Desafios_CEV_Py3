print('='*20,'DESAFIO 013','='*20,'\n')

salario = float(input('Digite o valor do salario: '))

novo_salario =  salario + ((salario/100)*15)

print('O novo salário é de R${:.2f}'.format(novo_salario))
