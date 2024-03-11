dia = int(input('Quantos dias alugados? '))
rod = int(input('Quantos Km rodados? '))
dia *= 60
rod *= 0.15
print(f'O total a pagar é de R${dia+rod:.2f}')
