nJogadores = int(input())
pontuacaoFinal = {}

for _ in range (nJogadores):
    entrada = input()
    pontuacaoFinal[entrada] = 0

rodadas = int(input())

for _ in range (rodadas):
    somaNum = 0
    valores = list(map(int, input().split()))
    somaNum = sum(valores)
    
    listaDePalpites = list(map(int, input().split()))
    cont = 0
    for jogador, pontos in pontuacaoFinal.items():
        if listaDePalpites[cont] == somaNum:
            pontuacaoFinal[jogador] = pontos + 1
        cont += 1

maior = 0    
vencedor = ''
resultado = ''
for chave, valor in pontuacaoFinal.items():
    if valor > maior:
        maior = valor
        vencedor = chave

for chave, valor in pontuacaoFinal.items():
    if chave != vencedor and maior == valor:
        resultado = 'EMPATE'
        break
    else:
        resultado = vencedor + ' GANHOU'

print(resultado)