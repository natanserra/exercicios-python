com1 = float(input('Digite o primeiro comprimento: '))
com2 = float(input('Digite o segundo comprimento: '))
com3 = float(input('Digite o terceiro comprimento: '))

if com1 < com2 + com3 and com2 < com1 + com3 and com3 < com2 + com1:
    print('Os segmentos acima podem formar um triangulo!!')

else:
    print('Os segmentos acima nao podem formar um triangulo')