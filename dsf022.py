#desafio 022

name = str(input('Digite seu nome completo'))
print(f"Seu nome em maiusculo:{name.upper()}")
print(f"Seu nome em minusculo:{name.lower()}")
print(f"Seu nome tem ao todo {len(name) - name.count(' ')} letras")
cut = name.split()
print(f"Seu primeiro nome é:{cut[0]} e tem {len(cut[0])}")