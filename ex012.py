preco = float(input('Qual é o preço do produto? R$'))
desc = preco - preco/100*5
print(f'O produto que custava R${preco}, na promoção com desconto vai de 5% vai custar R${desc:.2f}')
