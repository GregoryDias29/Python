
s = float(input('Qual é o salario do funcionario? R$ '))
c = s * 15 / 100
r = s + c
print('Um funcionario que ganhava {:.2f}, com 15% de aumento, passa a receber {:.2f}'.format(s,r))