a = int(input('Valor da reta 1'))
b = int(input('Valor da reta 2'))
c = int(input('Valor da reta 3'))

if ( ((b-c)<a<b+c) and ((a-c)<b<a+c) and ((a-c)<c<a+b) ):
	print('Formam um triângulo!')
else:
	print('Não formam um triângulo!')