# Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

n = float(input('Digite um numero para saber seu dobro, triplo e raiz quadrada: '))
n1 = n * 2
n2 = n * 3
n3 = pow(n,(1/2))#n **(1/2)
print('''O resultado é: 
dobro {}
triplo {}
Raiz {:.1f}'''.format(n1,n2,n3))