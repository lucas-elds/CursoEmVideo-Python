# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

aluno = []
for i in range(4):
    nome = input(f'Insira o nome do {i+1}° aluno: ').title()
    aluno.append(nome)

sort = random.choice(aluno)
print(f'O aluno sorteado foi: {sort}')

#sort = random.randint(0, 3)
#print(f'O aluno sorteado foi: {aluno[sort]}')
