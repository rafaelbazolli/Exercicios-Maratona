# Ainda não concluido

posicaoVeiculos = []; acidentes = 0
entrada = input()
linhas, colunas, numVeiculos = map(int, entrada.split())

for veiculo in range(numVeiculos):
    aux = []
    entrada = input()
    posX, posY, direcao = entrada.split()
    posX = int(posX); posY = int(posY)

    # Todas as possiveis localizações, seguindo suas respectivas direções
    if direcao == 'N':
        for i in range(posX, -1, -1):
            aux.append([i, posY])
    elif direcao == 'S':
        for i in range(posX, linhas):
            aux.append([i, posY])
    elif direcao == 'L':
        for i in range(posY, colunas):
            aux.append([posX, i])
    elif direcao == 'O':
        for i in range(posY, -1, -1):
            aux.append([posX, i])
    posicaoVeiculos.append(aux)

coordenadas_visitadas = set()
for veiculo in posicaoVeiculos:
    for posicao in veiculo:
        if tuple(posicao) in coordenadas_visitadas:
            acidentes += 1
        else:
            coordenadas_visitadas.add(tuple(posicao))

print(acidentes)
