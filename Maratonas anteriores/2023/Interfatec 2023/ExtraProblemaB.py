#Balas dumbinho 
soma = 0
entrada = str(input())

for elemento in entrada:
    soma += int(elemento)

print('dumbinho' if soma % 2 == 0 else '8-bonito')
