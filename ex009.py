num = int(input('Digite um número para ver sua tabuada: '))
cont = 1
print('------------')
while cont < 10:
    print(f'{num} x 0{cont} = {num*cont}')
    cont += 1

print(f'{num} x {10} = {num*10}')
print('------------')
