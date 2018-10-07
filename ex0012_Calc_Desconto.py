# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com desconto de 10% de desconto
v = float(input('Digite o valor do produto: R$'))
d = v * 40 / 100
r = v - d
print('O valor com desconto de 40% é : {}'.format(r))