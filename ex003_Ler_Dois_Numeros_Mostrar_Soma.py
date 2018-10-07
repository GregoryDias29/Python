# Crie um programa que leia dois números e mostre a soma entre eles
n1 = int(input('Digite o primeiro numero para ser somado: '))
n2 = int(input('Digite o segundo numero para ser com {}: '.format(n1)))
s = n1 + n2
print('O resultado entre {} + {} = {}'.format(n1,n2,s))