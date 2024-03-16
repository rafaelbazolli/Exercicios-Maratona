pousou = 0; pista = []
for x in input():
    if x == 'P':
        pousou += 1
        pista.append(pousou) #Só adiciona avião que pousou
    else:
        pista.pop() # Remove o ultimo 
print('Pista vazia' if not pista else pista)
