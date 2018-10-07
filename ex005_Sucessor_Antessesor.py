#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu atecessor
n = int(input('Digite um numero para saber seu antessecor e seu sucessor: '))
n1 = n - 1
n2 = n + 1
print('O antessesor de {} é o {} e o sucessor de {} é o {}'.format(n,n1,n,n2))
# tambem pode ser feito assim
#print ('Analisando o valor de {}, seu antecessor é {} e o seu sucessor {}.format(n, (n-1), (n+1)))
