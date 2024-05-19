qtdPerfis = input()
listaRegioesPessoas = []
perfisNecessarios = list(map(int, input().split()))
qtdRegioes = int(input())

for _ in range(qtdRegioes):
    entrada = list(input().split())
    crime = list(entrada[1:])
    listaRegioesPessoas.append([entrada[0], crime])

for elemento in listaRegioesPessoas:
    perfisAptos = 0
    menorValor = 0
    
    for i, pessoa in enumerate(elemento[1]):
        x = int(int(pessoa) / perfisNecessarios[i])
        
        if i == 0:
            menorValor = x
        else:
            if x < menorValor:
                menorValor = x
        if x == 0:
            menorValor = 0
            break
        
    elemento[1] = menorValor

for elem in listaRegioesPessoas:
    print(f'{elem[0]} {elem[1]}')
        