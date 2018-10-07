#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. calcule o preco a pagar, sabendo que o carro custa r$60 por dia e r$0,15 po KM rodado
km = float(input('Qual foi a quantidade de KM percorrido pelo carro alugado?: KM '))
dia = int(input('Qual foi a quantidade de dias que o carro foi alugado?: Dias '))
k = km * 0.15
d = dia * 60
r = k + d
print('A quantidade a ser paga é de R${:.2f}'.format(r))