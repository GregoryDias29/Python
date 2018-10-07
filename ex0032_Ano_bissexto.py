'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''
cores = {'limpo': '\033[m',
         'branco': '\033[4;30m',
         'vermelho ': '\033[4;31m',
         'verde': '\033[4;32m',
         'amarelo': '\033[4;33m',
         'azul': '\033[4;34m',
         'roxo': '\033[4;35m',
         'robi': '\033[4;36m'}
from datetime import date
print('\033[4;32m(Coloque 0 para analisar o ano atual)\033[m')
ano = int(input('\033[36mQue ano que vc quer analizar se é ou não \033[30mbissexto:\033[m '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100!= 0 or ano % 400 ==0:
    print('{}o ano{} {}{}{} {}é{} {}BISSEXTO'.format(cores['azul'],cores['limpo'],cores['amarelo'],ano,cores['limpo'],cores['azul'],cores['limpo'],cores['vermelho ']))
else:
    print('{}O ano{} {}{}{} {}Não{} {}é{} {}BISSEXTO'.format(cores['verde'],cores['limpo'],cores['amarelo'],ano,cores['limpo'],cores['vermelho '],cores['limpo'],cores['verde'],cores['limpo'],cores['roxo']))
