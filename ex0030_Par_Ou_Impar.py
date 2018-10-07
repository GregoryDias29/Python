# Crie um programa que leia um numero unteiro e mostre na tela se ele é PAR ou IMPAR
c = {'limpo': '\033[m',
         'branco': '\033[4;30m',
         'vermelho ': '\033[4;31m',
         'verde': '\033[4;32m',
         'amarelo': '\033[4;33m',
         'azul': '\033[4;34m',
         'roxo': '\033[4;35m',
         'robi': '\033[4;36m'}
numero = int(input('\033[4;36mDigite um numero para saber se é impar ou par:\033[m ').strip())
resultado = numero % 2
if resultado ==0:
    print('{}O numero{} {}{}{} {}é Par'.format(c['vermelho '],c['limpo'],c['amarelo'],numero,c['limpo'],c['vermelho '],c['vermelho ']))
else:
    print('{}O numero{} {}{}{} {}é Impar'.format(c['azul'],c['limpo'],c['amarelo'],numero,c['limpo'],c['azul']))
