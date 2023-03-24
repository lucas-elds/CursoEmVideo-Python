# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

txt = input('Insira algo: ')

print(f'\nTipo primitivo: {type(txt)}')
print(f'Alfanumérico: {txt.isalnum()}')
print(f'Alfabético: {txt.isalpha()}')
print(f'ASCII: {txt.isascii()}')
print(f'Decimal: {txt.isdecimal()}')
print(f'Dígito: {txt.isdigit()}')
print(f'Identificador: {txt.isidentifier()}')
print(f'Maiúsculo: {txt.isupper()}')
print(f'Minúsculo: {txt.islower()}')
print(f'Numérico: {txt.isnumeric()}')
print(f'Imprimível: {txt.isprintable()}')
print(f'Espaço: {txt.isspace()}')
print(f'Captalizado: {txt.istitle()}')
