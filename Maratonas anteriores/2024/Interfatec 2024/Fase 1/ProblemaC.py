valorAtualCarrinho, qtdRodadas = map(int, input().split())
alvo = 200 - valorAtualCarrinho
listaValores = []
dicioValores = {}
resultado = 'fretepago'

for _ in range(qtdRodadas):
    valor = int(input())
    listaValores.append(valor)

for valor in listaValores:
    if alvo - valor in dicioValores.keys():
        resultado = 'fretegratis'
    else:
        dicioValores[valor] = True
print(dicioValores)
print(resultado)
