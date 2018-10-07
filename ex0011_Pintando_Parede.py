# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade
#de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m²
l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l * a
print('Sua parede tem a dimensão de {} x {} e sua area é de {}m²'.format(l,a,area))
tinta = area / 2
print('Para pintar a parede vc precisa de {} litros de tinta'.format(tinta))