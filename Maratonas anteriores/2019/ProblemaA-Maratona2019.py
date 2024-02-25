def validarMatriz(matriz):
    # Se alguma linha é composta por 1
    for linha in matriz:
        if all(numero == 1 for numero in linha):
            return True
    # Se alguma coluna é composta por 1
    for coluna in range(len(matriz[0])):
        if all(linha[coluna] == 1 for linha in matriz):
            return True
    return False

# Entrada com as dimensões da sala e a quantidade de alarmes
entrada = str(input())

# Separando a string e criando a matriz
linhas, colunas, qtdAlarmes = map(int, entrada.split())
matriz = [[0] * colunas for _ in range(linhas)]

# Recebendo posição dos alarmes e sensibilidade
for alarme in range (qtdAlarmes):
    entrada = str(input())
    posX, posY, sense = map(int, entrada.split())
    posX -= 1
    posY -= 1
    
    # Modificando as casas ao redor do alarme para 1
    for i in range(posX + 1 - sense, posX + sense):   # Itera entre as linhas
        if 0 <= i < linhas:
            for j in range(posY + 1 - sense, posY + sense):  # Itera entre as colunas
                if 0 <= j < colunas:
                    matriz[i][j] = 1
                        
print('N' if validarMatriz(matriz) else 'S')
