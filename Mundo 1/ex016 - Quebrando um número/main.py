# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

num = float(input('Insira um número real: '))
print(f'A porção inteira de {num} é: {trunc(num)}')
