qtdPerfis = int(input())
perfisNecessarios = list(map(int, input().split()))
qtdRegioes = int(input())

listaRegioesPessoas = [[entrada[0], list(map(int, entrada[1:]))] for entrada in (input().split() for _ in range(qtdRegioes))]

for elemento in listaRegioesPessoas:
    elemento[1] = min((int(pessoa / perfisNecessarios[i]) for i, pessoa in enumerate(elemento[1])), default=0)

for elem in listaRegioesPessoas:
    print(f'{elem[0]} {elem[1]}')
