# def validarMatriz(matriz):
#     ''' Retornará True se não for possível passar, e false se tiver alguma possibilidade de atravessar a matriz'''
#     for linha in matriz:
#         if all((numero == '#') or (int(numero) > forca) for numero in linha):
#             return True
#     for coluna in range(len(matriz[0])):
#         if all((linha[coluna] == '#') or (int(linha[coluna]) > forca) for linha in matriz):
#             return True
#     return False

# forca = int(input()) # Força do Silas
# entrada = str(input()) # Dimensões do cenário
# linhas, colunas = map(int, entrada.split())
# cenario = []; aux = []

# for _ in range(linhas): # Recebendo as informações do cenário
#     entrada = str(input())
#     cenario.append(entrada.split())

# impossivel = validarMatriz(cenario) # Validando se há alguma linha ou coluna impossível de passar

# if(impossivel):
#     print('N')
# else:
#     # Implemente aqui o código para verificar se é possível chegar à última linha da matriz
#     fila = [(0, 0)]
#     visitado = set([(0, 0)])

#     while fila:
#         x, y = fila.pop(0)

#         if x == linhas - 1 and cenario[x][y] == 'K':
#             # Encontrou a chave, imprimir o número mínimo de movimentos necessários
#             print(visitado[(x, y)])
#             break

#         for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#             novo_x = x + dx
#             novo_y = y + dy

#             if novo_x >= 0 and novo_x < linhas and novo_y >= 0 and novo_y < colunas:
#                 if cenario[novo_x][novo_y] != '#' and (novo_x, novo_y) not in visitado:
#                     visitado.add((novo_x, novo_y))
#                     fila.append((novo_x, novo_y))
#     else:
#         # Não encontrou a chave, imprimir 'N'
#         print('N')