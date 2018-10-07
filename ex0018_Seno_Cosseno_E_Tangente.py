import math
d = float(input('Digite o algulo que vc deseja: '))
s = math.sin(math.radians(d))
c = math.cos(math.radians(d))
t = math.tan(math.radians(d))
print('O angulo de {} tem o SEN de {:.2f} \nO angulo de {} tem o COSSENO  de {:.2f}\nO angulo de {} tem a TANGENTE  de {:.2f}'.format(d,s,d,c,d,t))