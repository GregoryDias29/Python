#um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome deles e escrevendo o nome do escolhido
import random
a1 = input('Digite o nome do primeiro aluno para o sorteio: ')
a2 = input('Digite o segundo nome do aluno para o sorteio: ')
a3 = input('Digite o terceiro nome do aluno para o sorteado: ')
a4 = input('Digite o quarto nome do aluno para ser sorteado: ')
ale = [a1,a2,a3,a4]#uma lista em python fica em colchetes
es = random.choice(ale)
print('O alun escolido para apagar o quadro é {}'.format(es))