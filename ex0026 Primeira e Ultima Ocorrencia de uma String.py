# Faça um programa que leia um frase pelo teclado e mostre
# quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# em que posição ela aparece a ultima vez
f = str(input('Digite um frase: ')).upper().strip()
print('A quantidade de A que aparece é {}'.format(f.count('A')))
print('A posição que ela aparece a primeira vez é {}'.format(f.find('A')+1))
print('A posição que ela aparece por ultimo é {}'.format(f.rfind('A')+1))

