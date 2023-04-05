# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

import math
angulo = float(input('Ângulo: '))

seno = math.sin(math.radians(angulo))
print(f'Seno: {seno:.2f}')

cosseno = math.cos(math.radians(angulo))
print(f'Cosseno: {cosseno:.2f}')

tangente = math.tan(math.radians(angulo))
print(f'Tangente: {tangente:.2f}')
