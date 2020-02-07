#desafio 023
number = int(input('digite um número: '))

print(f'Unidade: {number // 1 % 10}')
print(f'Dezena: {number // 10 % 10}')
print(f'Centena: {number // 100 % 10}')
print(f'Milhar: {number // 1000 % 10}')