#desafio 026

frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print('n° de letras: {}'.format(frase.count('A')))
print('A primeira letra A está na posição {}'.format(frase.find('A')+1))
print('A última letra A está na posição {}'.format(frase.rfind('A')+1))