# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Insira um número: '))
dobro = num * 2
triplo = num * 3
raiz = num**(1 / 2)

print(f'\nDobro: {dobro}')
print(f'Triplo: {triplo}')
print(f'Raíz: {raiz:.2f}')
