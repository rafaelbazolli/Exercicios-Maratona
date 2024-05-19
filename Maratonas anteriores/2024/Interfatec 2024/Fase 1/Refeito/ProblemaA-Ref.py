qtdmapas = int(input())
valorRegioes = [] #superior, esquerda, centro, direita, inferior

for _ in range(qtdmapas):
    mapaAtual = []
    somaCentral = 0
    somaDireita = 0
    somaEsquerda = 0
    
    for i in range(6):
        entrada = list(map(int, input().split()))
        mapaAtual.append(entrada)
        
        if i == 0:
            somaSuperior = sum(entrada)
        elif i == 5:
            somaInferior = sum(entrada)
        else:
            somaCentral += 1 if entrada[1] == 1 else 0
            somaDireita += 1 if entrada[2] == 1 else 0
            somaEsquerda += 1 if entrada[0] == 1 else 0
    
    parcial = [somaSuperior, somaEsquerda, somaCentral, somaDireita, somaInferior]
    maiorValor = max(parcial)
    pos_anterior = None

    for i in range(len(parcial)):
        if parcial[i] == maiorValor:
            posicao_anterior = i - 1 if i > 0 else None
            break

    valorRegioes.append()

# Aqui valorRegioes ja tem as somas de cada região dos mapas