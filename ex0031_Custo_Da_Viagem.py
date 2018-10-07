#Desenvolva um programa que pergunte a distancia de uma viagem em KM. CALCULE o PREÇO da passagem, cobrando R$0,50
# por km para viagens de até 200km e r$0,45 para a viagens mais longa
cores = {'limpo': '\033[m',
         'branco': '\033[4;30m',
         'vermelho ': '\033[4;31m',
         'verde': '\033[4;32m',
         'amarelo': '\033[4;33m',
         'azul': '\033[4;34m',
         'roxo': '\033[4;35m',
         'robi': '\033[4;36m'}
distancia = float(input("\033[4;35mDigite a distancia de sua viagem em Km:\033[m ").strip())
print('{}Você está prestes a começar uma viagem de{} {}{}Km.{}'.format(cores['azul'],cores['limpo'],cores['amarelo'],distancia,cores['limpo']))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('{}O valor da sua passagem  é: {}{}R${:.2f}'.format(cores['robi'],cores['limpo'],cores['vermelho '],preco))


