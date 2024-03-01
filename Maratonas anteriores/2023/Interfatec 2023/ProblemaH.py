entrada = int(input())
if(entrada <= 107):
    saida = entrada + 7
else:
    saida = entrada + (entrada * 0.07)
print(round(saida))