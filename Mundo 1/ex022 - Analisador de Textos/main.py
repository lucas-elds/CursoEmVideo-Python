# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = input('Insira seu nome completo: ')
print(f'Maiúsculo: {nome.upper()}')
print(f'Minúsculo: {nome.lower()}')
print(f'Tamanho nome: {len(nome.replace(" ", ""))}')
print(f'tamanho 1º nome: {len(nome.split()[0])}')
