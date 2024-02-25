entrada = str(input())
linhas, tipo = entrada.split()
linhas = int(linhas)
alfabeto = 'abcdefghijklmnopqrstuvwxyz'; aux = 1; ref = 25

for _ in range(linhas):
    if(tipo == 'minusculas'):
        palavra1 = ('.' * ref).strip()
        palavra2 = alfabeto[:aux].strip()
        print(palavra1 + palavra2)
    elif(tipo == 'maiusculas'):
        palavra1 = ('.' * ref).strip().upper()
        palavra2 = alfabeto[:aux].strip().upper()
        print(palavra1 + palavra2)
    aux += 1
    ref -= 1