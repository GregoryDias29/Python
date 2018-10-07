# Crie um programa que leia quanros dinheiro uma pessoa tem na sua carteira e mostre quantos dolares ela
#pode comprar. (considera uss1,00 = r$3,26)
r = float(input('Quanto dinheiro vc tem na sua carteira ? R$ '))
d = r / 3.29
dc = r / 2.57
eu = r / 3.88
li = r / 4.40
print('Com {:.2f}R$ vc pode comprar: \nDOLAR: {:.2f} \nDOLAR CANADENCE: {:.2f} \nEURO: {:.2f} \nLIBRA: {:.2f} '.format(r,d,dc,eu,li))
