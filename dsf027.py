#desafio027
name = str(input('Digite seu nome completo: ')).strip()
brokeName = name.split()
print(f'Seu primeiro nome é: {brokeName[0]}')
print(f'Seu primeiro nome é: {brokeName[len(brokeName)-1]}')