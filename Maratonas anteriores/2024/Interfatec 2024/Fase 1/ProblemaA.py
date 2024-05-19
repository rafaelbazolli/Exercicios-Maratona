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
    valorRegioes.append([somaSuperior, somaEsquerda, somaCentral, somaDireita, somaInferior])

    
listaSeila = []    # o indice do maior de cada lista 
for i, item in enumerate(valorRegioes):
    indiceDoMaior = 0
    maior = max(item)
    
    for i, elemento in enumerate(item):
        if elemento == maior:
            indiceDoMaior = i
            break
    
    listaSeila.append(indiceDoMaior)

listaFinal = []
for item in listaSeila:
    superior = 0; esquerda = 0; centro = 0; direita = 0
    inferior = 0
    
    if item == 0:
        superior += 1
    elif item == 1:
        esquerda += 1
    elif item == 2:
        centro += 1
    elif item == 3:
        direita += 1
    else:
        inferior += 1
            
    listaFinal.append(superior)
    listaFinal.append(esquerda)
    listaFinal.append(centro)
    listaFinal.append(direita)
    listaFinal.append(inferior)

for i, item in enumerate(listaFinal):
    indiceDoMaior2 = 0
    maior = max(item)
    
    for i, elemento in enumerate(item):
        if elemento == maior:
            indiceDoMaior2 = i
            break

if indiceDoMaior2 == 0:
    print('superior')
elif indiceDoMaior2 == 1:
    print('esquerda')
elif indiceDoMaior2 == 2:
    print('centro')
elif indiceDoMaior2 == 3:
    print('direita')
else:
    print('inferior')