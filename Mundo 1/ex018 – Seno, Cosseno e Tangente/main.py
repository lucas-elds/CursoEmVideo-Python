# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 

import math
angulo = float(input('Ângulo: '))

seno = math.sin(math.radians(angulo))
print('Seno: {seno:.2f}')

cosseno = math.cos(math.radians(angulo))
print('Cosseno: {cosseno:.2f}')

tangente = math.tan(math.radians(angulo))
print('Tangente: {tangente:.2f}')
