alunos = int(input('Digite o número de alunos: '))
provas = []
atividades = []
alteradas = 0

for i in range(alunos):
    provas.append(float(input('Digite uma nota de prova: ')))

for i in range (alunos):
    atividades.append(float(input('Digite uma nota de atividade:')))

for aluno in range(alunos):
    if atividades[aluno] == 10.00 and provas[aluno] != 10.00:
        alteradas += 1

print(f'NOTAS ALTERADAS: {alteradas}')

for aluno in range(alunos):
    if atividades[aluno] == 10.00 and provas[aluno] != 10.00:       
        provas[aluno] += 2.00
        if provas[aluno] > 10.00:
            print(f'*(00{aluno+1}) original: {provas[aluno]-2.00:05.2f} | final: 10.00')
        else:
            print(f'*(00{aluno+1}) original: {provas[aluno]-2.00:05.2f} | final: {provas[aluno]:05.2f}')
    else:
        print(f'-(00{aluno+1}) original: {provas[aluno]:05.2f} | final: {provas[aluno]:05.2f}')