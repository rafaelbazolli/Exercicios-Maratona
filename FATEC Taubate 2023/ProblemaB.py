def validarTipoExpressao(expressao):
    if(len(expressao) == 5): return 'tipo1'
    elif(len(expressao) == 11): return 'tipo2'
    elif(len(expressao) == 13): return 'tipo3'
    elif(len(expressao) == 25): return 'tipo4'
    elif(len(expressao) == 19):
        if(expressao[4] == ')'): return 'tipo6'
        else: return 'tipo5'
                 
                 
# Variaveis                  
corDeSaida = ''
aux1 = False
aux2 = False    
cores = [['AMR', 'LAR', 'VML'], ['LAR', 'AMR', 'VML'], ['VML', 'AMR', 'LAR'], ['AMR', 'VML', 'LAR'],
         ['AZL', 'VML', 'RXO'], ['VML', 'AZL', 'RXO'], ['AMR', 'AZL', 'VRD'], ['AZL', 'AMR', 'VRD'],
         ['AMR', 'VRD', 'AZL'], ['VRD', 'AMR', 'AZL'], ['BRC', 'PRT', 'CNZ'], ['PRT', 'BRC', 'CNZ'],
         ['VML', 'BRC', 'RSA'], ['BRC', 'VML', 'RSA'], ['LAR', 'BRC', 'BJE'], ['BRC', 'LAR', 'BJE'],
         ['VML', 'VRD', 'MRN'], ['VRD', 'VML', 'MRN'], ['LAR', 'RXO', 'MRT'], ['RXO', 'LAR', 'MRT'],
         ['RXO', 'BRC', 'LLS'], ['BRC', 'RXO', 'LLS']]


# Recebendo a expressao
expressao = str(input())
tipoExpressao = validarTipoExpressao(expressao)  # 'tipo4'

for elemento in cores:  # cores[0][0]
    if(tipoExpressao == 'tipo1'):  ## Tipo 1   (cor)
        if(expressao[1:4] == elemento[2]): corDeSaida = expressao[1:4]; break  
        
    elif(tipoExpressao == 'tipo2'): ## Tipo 2   (cor + cor)
        if(expressao[1:4] == expressao[7:10]): corDeSaida = expressao[1:4]; break  ## Validar se as duas cores tem o mesmo valor
        if(elemento[0] == expressao[1:4] and elemento[1] == expressao[7:10]):
            corDeSaida =  elemento[2]; break            
            
    elif(tipoExpressao == 'tipo3'): ## Tipo 3   (cor) + (cor)
        if(expressao[1:4] == expressao[9:12]): corDeSaida = expressao[1:4]; break
        if(elemento[0] == expressao[1:4] and elemento[1] == expressao[9:12]):
            corDeSaida =  elemento[2]; break   
            
    elif(tipoExpressao == 'tipo4'): ## Tipo 4   (cor + cor) + (cor + cor)
        # Validando se alguma parte das expressões está com cores iguais
        if(expressao[1:4] == expressao[7:10]): aux1 = expressao[1:4]
        if(expressao[15:18] == expressao[21:24]): aux2 = expressao[15:18]
        
        if(elemento[0] == expressao[1:4] and elemento[1] == expressao[7:10]):
            aux1 =  elemento[2]      
        if(expressao[15:18] == expressao[21:24]): aux2 = expressao[15:18]
        if(elemento[0] == expressao[15:18] and elemento[1] == expressao[21:24]): 
            aux2 =  elemento[2]      
        if(aux1 and aux2):
            novaExpressao = f'({aux1} + {aux2})'
            if(aux1 == aux2): corDeSaida = aux1; break
            for elemento in cores:
                if(elemento[0] == novaExpressao[1:4] and elemento[1] == novaExpressao[7:10]):
                    corDeSaida =  elemento[2]; break      
                                  
    elif(tipoExpressao == 'tipo5'): ## Tipo 5    (cor + cor) + (cor)
        if(expressao[1:4] == expressao[7:10]): corDeSaida = expressao[1:4]
        if(elemento[0] == expressao[1:4] and elemento[1] == expressao[7:10]):
            aux1 =  elemento[2]            
        if(aux1):
            novaExpressao = f'({aux1} + {expressao[15:18]})'
            if(novaExpressao[1:4] == novaExpressao[7:10]): corDeSaida = novaExpressao[1:4]; break
            for elemento in cores:
                if(novaExpressao[1:4] == novaExpressao[7:10]): corDeSaida = novaExpressao[1:4]; break
                if(elemento[0] == novaExpressao[1:4] and elemento[1] == novaExpressao[7:10]):
                    corDeSaida =  elemento[2]; break        
                        
    elif(tipoExpressao == 'tipo6'): ## Tipo 6   (cor) + (cor + cor)
        if(expressao[9:12] == expressao[15:18]): corDeSaida = expressao[9:12]
        if(elemento[0] == expressao[9:12] and elemento[1] == expressao[15:18]):
            aux1 =  elemento[2]            
        if(aux1):
            novaExpressao = f'({expressao[1:4]} + {aux1})'
            if(expressao[1:4] == expressao[7:10]): corDeSaida = expressao[1:4]
            for elemento in cores: 
                if(elemento[0] == novaExpressao[1:4] and elemento[1] == novaExpressao[7:10]):
                    corDeSaida =  elemento[2]; break  
                                  
    if(elemento == cores[-1]):  # Se fez todas as iterações no vetor de cores e nenhuma foi valida
        corDeSaida = 'ESCOLHA VOCE MESMO'; break                   
print(corDeSaida)
