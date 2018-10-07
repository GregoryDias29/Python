# escreva um progrma que leia um valor em metros e o exiba convertido em centimetros e milimetros
v = float(input('Escreva um valor em metros para ser convertido em centimetros e milimetros: '))
km = v / 1000
hm = v / 100
dam = v / 10
dm = v * 10
cm = v * 100
mm = v * 1000
print('A medida de {}m corresponde a {}km, {}hm, {}dam, {}dm , {}cm, {}mm'.format(v,km,hm,dam,dm,cm,mm))
