# Problema E - Exibição de Peixes

vetorPeixes = []; femeasParaMover = 0; aux = 0
qtdTanques = int(input())

for tanque in range(qtdTanques):        
    entrada = str(input())
    vetorPeixes.append(list(map(int, entrada.split())))

vetorPeixesOrdenado = sorted(vetorPeixes, key=lambda elemento: elemento[-1], reverse=True)
tanqueReferencia = vetorPeixesOrdenado[0]
vetorPeixesOrdenado.pop(0)

for tanque in vetorPeixesOrdenado:
    femeasParaMover += tanque[1]
    aux += tanque[0]

totalMachos = aux + tanqueReferencia[0]
movimentos = (femeasParaMover + (totalMachos + 1)) if (aux < totalMachos) else (femeasParaMover + (totalMachos - 1))
print(movimentos)
