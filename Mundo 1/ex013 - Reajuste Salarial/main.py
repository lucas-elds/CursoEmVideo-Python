# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Insira o salário: R$ '))
aumento = salario + (salario * 0.15)

print(f'\nO novo salário com um aumento de 15% será de R$ {aumento:.2f}')
