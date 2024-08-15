salario = float(input('Digite o seu salário: '))

if salario <= 1250:
    novosal = salario + (salario * 15/100)
else:
    novosal = salario + (salario * 10/100)

print(f'Seu salário era {salario} e passou a ser {novosal}')
