# Problema B - Bobo da corte

candidatos = []
numCandidados = int(input())

for candidato in range(numCandidados):
    votos = int(input())
    candidatos.append(votos)

# Votos do Carlos, e removendo ele da listagem
votosCarlos = candidatos[0]
candidatos.pop(0)

candidatosOrdenado = sorted(candidatos, reverse=True)

print('S' if votosCarlos >= candidatosOrdenado[0] else 'N')
