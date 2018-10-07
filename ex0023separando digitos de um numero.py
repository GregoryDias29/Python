# Faça um programa que leua um numero de 0 a 9999 emostre na tela cada um dos digitos separados
# ex: dite um numero: 1834
# unidade: 4 dezena 3 centena 8 milhar:1
n = int(input('Informe um numero: '))
#n1 = str(n)
#print('Unidade: {}\n Dezena: {}\nCentena: {}\n Milhar: {}'.format(n1[3],n1[2],n1[1],n1[0]))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u,d,c,m))