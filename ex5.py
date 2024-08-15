custo = float(input('Digite a distancia percorrida na viagem: '))

if custo < 200:
    resultado = custo *0.50
    print(f'O custo da viagem foi R${resultado}')
else:
    resultado = custo * 0.45
    print(f'O custo da viagem foi R${resultado}')