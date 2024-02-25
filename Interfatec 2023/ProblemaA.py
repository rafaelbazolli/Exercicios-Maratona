contagem = 0; livros = []
qtdLivros = int(input())
livrosFinal = list(input())

for i in range(qtdLivros - 1): 
    for j in range(qtdLivros - i - 1): # A cada iteração, o range diminui, pois já terá sido validado um livro(da direita pra esquerda)
        if livrosFinal[j] > livrosFinal[j + 1]:  # Se o anterior for maior que o próximo, inverte a posição
            livros.append(livrosFinal[j])   # Armazena em livros, qual livro foi trocado de lugar(qual foi lido)
            livrosFinal[j], livrosFinal[j + 1] = livrosFinal[j + 1], livrosFinal[j]
            contagem += 1

# Validando se algum estudante pegou livro mais de 5x
repeticoes = [livros.count(livro) for livro in livros] # Conta quantas vezes cada livro foi movido
estudanteDBPegou = any(frequencia > 5 for frequencia in repeticoes)

print('A Database Systems student read a book.' if (estudanteDBPegou) else contagem)
