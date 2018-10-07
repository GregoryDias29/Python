# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
# EX ana maria de souza
#primeiro ana
#segundo souza
d = str(input('Digite seu nome completo: ')).strip().title()
nome = d.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))#menos um por que tem um amenos ele começa apartir do 0



