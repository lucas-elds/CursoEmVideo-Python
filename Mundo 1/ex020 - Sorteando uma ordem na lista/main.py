# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno = []
for i in range(4):
    nome = input(f'Insira o nome do {i+1}° aluno: ').title()
    aluno.append(nome)

random.shuffle(aluno)
print('\nOrdem das apresentações:')

for i in range(4):
    print(f'{i+1}° - {aluno[i]}')
