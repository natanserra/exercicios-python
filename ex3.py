velo = int(input('Digite a velocidade: '))

if velo >=80:
    print(f'Voce passou acima do permitido')
    multa = velo * 7
    print(f'Voce foi multado em R${multa}')

else:
    print('Tenha um Bom dia!!')