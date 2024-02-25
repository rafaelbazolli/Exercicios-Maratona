# Definição dos modelos de venda
def modelo1(produtos, qtdVendida, totalEstoque):  ## Compra mais antiga
    totalVendaM1 = 0; aux = produtos[0][0]
    if qtdVendida <= aux:  # Se a quantidade vendida foi menor do que a qtd de produtos do primeiro item
        return totalEstoque - (qtdVendida * produtos[0][1])
    else:  # Se a quantidade vendida ultrapassa a qtd de produtos do primeiro item
        totalVendaM1 = (produtos[0][2])
        aux = qtdVendida - produtos[0][0]
        for produto in produtos[1:]:
            if(aux <= produto[0]):
                return totalEstoque - (totalVendaM1 + (aux * produto[1]))
            else:
                totalVendaM1 += (aux * produto[1])
            aux -= produto[0]

def modelo2(produtos, qtdVendida, totalEstoque):  ## Compra mais recente
    totalVendaM2 = 0; aux = produtos[-1][0]
    if qtdVendida <= aux:  # Se a quantidade vendida foi menor do que a qtd de produtos do primeiro item
        return totalEstoque - (qtdVendida * produtos[-1][1])
    else:  # Se a quantidade vendida ultrapassa a qtd de produtos do primeiro item
        totalVendaM2 = produtos[-1][2]
        aux = qtdVendida - produtos[0][0]
        for produto in produtos[-2::-1]: # preciso percorrer esse for ao contrario
            if(aux <= produto[0]):
                # print(f'Modelo 2. Tá errado isso então = {totalVendaM1}')
                return totalEstoque - (totalVendaM2 + (aux * produto[1]))
            else:
                totalVendaM2 += (aux * produto[1])
            aux -= produto[0]

def modelo3(produtos, qtdVendida, totalEstoque, totalProdutos):  ## Média das compras
    return totalEstoque - ((totalEstoque / totalProdutos) * qtdVendida)

produtos = []; totalEstoque = 0; totalProdutos = 0
while(True):
    entrada = str(input())

    if ' ' in entrada:  ## Se tiver espaço é porque o usuario inseriu produtos
        qtd, valor = map(float, entrada.split())
        custo = qtd * valor
        produtos.append([qtd, valor, custo])
    
    elif entrada.startswith('V'):  ## Nesse caso ele inseriu a string para venda V{inteiro}
        qtdVendida = entrada[1:]
        
        # Calcular o total do estoque, antes de chamar as funções
        for produto in produtos: totalEstoque += produto[2]; totalProdutos += produto[0]
        
        M1 = (modelo1(produtos, int(qtdVendida), totalEstoque))
        M2 = (modelo2(produtos, int(qtdVendida), totalEstoque))
        M3 = (modelo3(produtos, int(qtdVendida), totalEstoque, totalProdutos))
        modelo1 = "{:.2f}".format(M1).replace(".", ",")
        modelo2 = "{:.2f}".format(M2).replace(".", ",")
        modelo3 = "{:.2f}".format(M3).replace(".", ",")      
         
        if(M1 == M2 and M2 == M3): print(f'TODOS IGUAIS = R${modelo1}')
        elif(M1 == M2) and (M1 < M3): print(f'M1 ou M2 = R${modelo2}')
        elif(M1 == M3) and (M1 < M2): print(f'M1 ou M3 = R${modelo1}')
        elif(M2 == M3) and (M2 < M1): print(f'M1 ou M3 = R${modelo1}')
        elif(M1 < M2) and (M1 < M3): print(f'M1 = R${modelo1}')
        elif(M2 < M1) and (M2 < M3): print(f'M2 = R${modelo2}')
        elif(M3 < M1) and (M3 < M2): print(f'M3 = R${modelo3}')
        break
