# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = int(input('Quantos km foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
valor = (60.0 * dias) + (0.15 * km)

print(f'O valor total a ser pago é: R$ {valor:.2f}')
