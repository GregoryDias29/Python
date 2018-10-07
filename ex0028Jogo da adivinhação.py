#Escreva un programa que faça o computador 'pensar' em um numero interiro entre 0 e 5
#e faça para o usuario tentar descobrir qual foi o umero escolido pelo computador. o programa devera escrever na tela
#se o usuario venceu ou perdeu
c = {'limpo': '\033[m',
         'branco': '\033[4;30m',
         'vermelho ': '\033[4;31m',
         'verde': '\033[4;32m',
         'amarelo': '\033[4;33m',
         'azul': '\033[4;34m',
         'roxo': '\033[4;35m',
         'robi': '\033[4;36m'}
from random import randint
from time import sleep
#faz o computador 'pensar'
c = randint(0 , 5)# faz ele sortear
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
j = int(input('Em que numero eu pensei? ').strip())#jogador tenta adivinhar
print('Procesando...')
sleep(3)
if j == c:
    print('Parabens vc ganhou o game.')
else:
    print('Vc perdeu louser eu pensei no {} e não no {}'.format(c,j))

