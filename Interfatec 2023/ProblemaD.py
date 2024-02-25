# entrada = str(input()) # Lendo numero de empresas e o padrão de transporte
# numEmpresas, padrao = map(int, entrada.split())

# dias = int(input())
# trocas = []; trocasDoDia = []; empresas = [[0] * numEmpresas for _ in range(numEmpresas)] # A lista empresas vai armazenar qtd de botijões que cada um tem

# # empresas[0] seria a empresa 1... // trocasDoDia irá armazenar quais empresas torcaram , e quantas viajens foram feitas

# for dia in range(dias):
#     entrada = input() # Texto do dia, que será ignorado
#     aux = 0
#     for i in range(numEmpresas * 2):  # As entradas serão o dobro da qtd de empresas
#         entrada = str(input())
#         origem, destino, numBotijoes = map(int, entrada.split())
        
#         empresas[origem-1][destino-1] += numBotijoes 
        
#         if(empresas[origem-1][destino-1] >= empresas[destino-1][origem-1]): # Se as duas tiverem qtd igual ou maior, haverá troca
#             aux += 1
#             # Verificando quantas viajens serão necessárias
#             viajensOD = empresas[origem-1][destino-1] // padrao
#             viajensDO = empresas[destino-1][origem-1] // padrao
#             if(viajensOD >= 1) or (viajensDO >= 1):
#                 pass            ############
            
#     if aux == 0:
#         trocas.append(0)
#     else:
#         trocas.append(trocasDoDia)

# cont = 1
# for troca in trocas:
#     print(f'Final dia {cont}')
#     if troca == 0:
#         print(' Sem Trocas')
#     else:
#         for i in troca: ## Caso existam trocas naquele dia, será uma lista 
#             print(f' Trocas entre {}({}v) e {}({}v)')
             
        
