# Criando a tupla com os números por extenso
numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                   'seis', 'sete', 'oito', 'nove', 'dez',
                   'onze', 'doze', 'treze', 'catorze', 'quinze',
                   'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    # Lendo o número do usuário
    numero = int(input('Digite um número entre 0 e 20: '))

    # Verificando se o número está no intervalo correto
    if 0 <= numero <= 20:
        break
    print('Tente novamente. ', end='')

# Mostrando o número por extenso
print(f'Você digitou o número {numeros_extenso[numero]}.')