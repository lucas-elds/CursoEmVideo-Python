# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print('Insira a largura e a altura da parede em metros:')
largura = float(input('\nLargura: '))
altura = float(input('Altura: '))
area = altura * largura
litro = area / 2
print(f'\nPara pintar uma área de {area:.2f}m² é preciso utilizar {litro:.1f}L de tinta.')
