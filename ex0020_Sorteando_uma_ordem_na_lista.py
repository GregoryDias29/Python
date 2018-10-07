# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos
#faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quaro aluno: ')
lista = [a1,a2,a3,a4]
random.shuffle(lista)

print('A ordem de apresentação será: {}'.format(lista))