# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
#hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
hipotenusa = hypot(co, ca)
print(f'A hipotenusa é: {hipotenusa:.2f}')
