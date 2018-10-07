# Faca um programa que leia tres numeros e mostre qual é o maior e qual é o menor.
cores = {'limpo': '\033[m',
         'branco': '\033[4;30m',
         'vermelho ': '\033[4;31m',
         'verde': '\033[4;32m',
         'amarelo': '\033[4;33m',
         'azul': '\033[4;34m',
         'roxo': '\033[4;35m',
         'robi': '\033[4;36m'}
n1 = int(input('\033[4;31mPrimeiro valor:\033[m ').strip())
n2 = int(input('\033[4;33mSegundo valor:\033[m ').strip())
n3 = int(input('\033[4;0;34mTerceiro valor:\033[m ').strip())
# Verifica quem é o menor
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificar quem é o maior
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('{}O{} {}menor{} {}valor digitado é{} {}{}{}'.format(cores['roxo'], cores['limpo'], cores['amarelo'],
                                                           cores['limpo'], cores['roxo'], cores['limpo'],
                                                           cores['branco'], menor, cores['limpo']))
print('{}O{} {}maior{} {}valor digitado é{} {}{}'.format(cores['robi'], cores['limpo'], cores['verde'], cores['limpo'],
                                                         cores['robi'], cores['limpo'], cores['vermelho '], maior))
