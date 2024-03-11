sal = float(input('Qual o salário do Funcionário? R$'))
aum = sal + sal/100*15
print(f'Um funcionário que ganhava R${sal}, com 15% de aumento, passa a receber R${aum:.2f}')
