# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Preço do produto: R$ '))
desconto = valor - (valor * 0.05)
print(f'O valor R$ {valor:.2f} com um desconto de 5% é: R$ {desconto:.2f}')
