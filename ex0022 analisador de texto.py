n = input('Digite seu nome completo: ').strip()
m = n.upper()
mi = n.lower()
q = len(n) - n.count(' ')
l = n.find(' ')
print('Seu nome em maiusculo fica: {}\nseu nome em minusculo fica: {}\nSeu nome tem ao todos {} letras'.format(m,mi,q,))
#poderia ter feiro assim
separa = n.split()
print ('Seu primeiro nome é {} e ele tem {} letras '. format(separa[0], len (separa[0])))