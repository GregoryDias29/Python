# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km, mostre uma mensagem dizendo que ele foi multado
# a multa vai custar R$ 7,00 por kmacima da velocidade
cores = {'limpo': '\033[m',
         'branco': '\033[4;30m',
         'vermelho ': '\033[4;31m',
         'verde': '\033[4;32m',
         'amarelo': '\033[4;33m',
         'azul': '\033[4;34m',
         'roxo': '\033[4;35m',
         'robi': '\033[4;36m'}
velocidade = float(input('Digite a velocidade do veiculo: ').strip())
if velocidade > 80:
    print('\033[1;31mMultado! O carro esedeu o limite de velocidade!')
    multa = (velocidade - 80) * 7
    print('O motorista devera pagar uma multa de {}{:.2f}{}'.format(cores['amarelo'],multa,cores['limpo']))
else:
    print('{}O carro esta na velocidade permitida!'.format(cores['verde']))
