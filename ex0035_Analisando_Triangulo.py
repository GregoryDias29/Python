# Desenvolvs um progrma que leia o comprimento de tres retas e diga ao usuario se eleas podem ou n'ao formar um triangulo
cores = {'limpo': '\033[m',
         'branco': '\033[1;30m',
         'vermelho ': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m',
         'robi': '\033[1;36m'}
print('\033[1;36m-=-\033[m'*8)
print('\033[1;33mAnalizador de Triangulos\033[m')
print('\033[1;36m-=-\033[m'*8)
r1 = float(input('\033[1;34mPrimeiro seguimento: \033[m').strip())
r2 = float(input('\033[1;32mSegundo seguimento: \033[m').strip())
r3 = float(input('\033[1;31mTerceiro seguimento: \033[m').strip())
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('{}Os segmentos acima{} {}pode{} {}formar triangulo!{}'.format(cores['branco'],cores['limpo'],
                                                                         cores['roxo'],cores['limpo'],
                                                                         cores['branco'],cores['limpo']))
else:
    print('{}Os segmentos acima{} {}não{} {}podem formar triangulo!{}'.format(cores['robi'],cores['limpo'],
                                                                              cores['amarelo'],cores['limpo'],
                                                                              cores['robi'],cores['limpo']))
