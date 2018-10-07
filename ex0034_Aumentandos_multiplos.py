# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# para salarios superiores a R$1,250,00, calcule um aumento de 10%.
# para os inferiores ou iguais, o aumento é de 15%.
cores = {'limpo': '\033[m',
         'branco': '\033[4;30m',
         'vermelho ': '\033[4;31m',
         'verde': '\033[4;32m',
         'amarelo': '\033[4;33m',
         'azul': '\033[4;34m',
         'roxo': '\033[4;35m',
         'robi': '\033[4;36m'}
pergunta = float(input('\033[4;35mQual é o salário do funcionario?\033[m \033[4;30mR$\033[m').strip())
alto = pergunta * 10 / 100
resalto = pergunta + alto
baixo = pergunta * 15 / 100
resbaixo = pergunta + baixo
if pergunta >= 1250.00:
    alto = resalto
    print('{}Quem ganhava{} {}R$:{:.2f}{} {}passa a ganhar{} {}R$:{:.2f}{} {}agora.{}'.format(cores['verde'],cores['limpo'],cores['vermelho '],pergunta,cores['limpo'],
                                                                                    cores['verde'],cores['limpo'],cores['vermelho '],resalto,cores['limpo'],
                                                                                    cores['verde'],cores['limpo']))
else:
    print('{}Quem ganhava{} {}R$:{:.2f}{} {}passa a ganhar{} {}R$:{:.2f}{} {}agora{} '.format(cores['azul'],cores['limpo'],cores['amarelo'],pergunta,cores['limpo'],cores['azul'],
                                                                      cores['limpo'],cores['amarelo'],resbaixo,cores['limpo'],cores['azul'],cores['limpo']))




