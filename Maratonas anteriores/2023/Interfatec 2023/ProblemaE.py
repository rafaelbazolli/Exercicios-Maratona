entrada = str(input()) # Leitura da primeira linha, linhas, coluna e carga
linhas, colunas, carga = map(int, entrada.split())

entrada = str(input()) # Localização do Crausio
lin, col = map(int, entrada.split()) 

crausio = [lin - 1, col - 1]
entrada = str(input()) # String da movimentação # Exemplo: CDCBEDBECB
bateu = 0

for letra in entrada: 
    if carga > 0:
        carga -= 1
        if letra == 'C':
            if crausio[1] <= 0: # Bateu em cima
                bateu += 1
            else:
                crausio[1] -= 1 # Andou pra cima                
        if letra == 'B':
            if crausio[1] >= colunas: # Bateu em baixo
                bateu += 1
            else: 
                crausio[1] += 1 # Andou pra baixo 
        if letra == 'E':
            if crausio[0] <= 0: # Bateu na esquerda
                bateu += 1
            else:
                crausio[0] -= 1 # Andou pra esquerda
        if letra == 'D':
            if crausio[0] >= linhas: # Bateu na direita
                bateu += 1
            else:
                crausio[0] += 1 # Andou pra direita
print(crausio[1] + 1, crausio[0] + 1, bateu)