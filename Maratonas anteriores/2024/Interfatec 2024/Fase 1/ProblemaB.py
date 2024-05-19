lista = {'ABC': 2,
         'DEF': 3,
         'GHI': 4,
         'JKL': 5,
         'MNO': 6,
         'PQRS': 7,
         'TUV': 8,
         'WXYZ': 9}

numPalavras = int(input())
listaNumeros = []

for _ in range (numPalavras):
    palavra = input()
    numero = ''
    for letra in palavra:
        for item in lista: #lista
            if letra in item:
                numero = numero + str(lista[item])
    listaNumeros.append(numero)

for numero in listaNumeros:
    print(numero)

