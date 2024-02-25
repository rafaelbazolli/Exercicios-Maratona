num_classificados = 0; maior = 0
pontuacao = []

competidores = int(input())

for i in range(0, competidores):
        min_competidores = int(input())
        
        if(min_competidores < 1 or min_competidores > competidores):
            pass
        else:
            for i in range(1, competidores + 1):  ## Faz a leitura dos competidores
                pontuacao_atual = int(input())
                pontuacao.append(pontuacao_atual)
                
            pontuacao.sort(reverse=True)
            pontuacao_ordenado = pontuacao  ## Reverte a lista de pontuações para Decrescente
            
            classificados = pontuacao_ordenado[:min_competidores]  ## Pega a primeira parte da pontuação até o mínimo
            aux = pontuacao_ordenado[min_competidores - 1]  ## Armazena o último valor existente no range do mínimo de competidores
            
            for item in pontuacao_ordenado[min_competidores:]:   ## Fatia a lista ordenada do minimo até o fim
                if(item == aux):
                    classificados.append(aux)
            
            print(len(classificados)) 
            break