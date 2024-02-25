# Problema G - Guardando Enfeites
vetorEntradas = []; vetorOrdenado = []
qtdEnfeites = int(input())

for enfeite in range(qtdEnfeites):
    entrada = str(input())
    vetorEntradas.append(list(map(int, entrada.split())))

for i in range(qtdEnfeites):
    indiceMaior = 0; maior = 0

    for j, elemento in enumerate(vetorEntradas[i]):   # elemento é cada numero na linha[i] do vetor de entradas. 'j' é o índice desse elemento
        if elemento > maior:
            if j+1 in vetorOrdenado: # Se o índice desse elemento ja estiver na lista, pula pra fora da condicional
                continue
            else:
                maior = elemento
                indiceMaior = j+1
    vetorOrdenado.append(indiceMaior)

for item in vetorOrdenado:
    print(item, end=' ')
