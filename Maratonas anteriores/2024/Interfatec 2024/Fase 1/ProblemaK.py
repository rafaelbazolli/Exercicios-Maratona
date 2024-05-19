numero = int(input())
contDivisivel = 0
    
for x in range(1, numero+1):
    if numero % x == 0:
        contDivisivel += 1
print('sim' if contDivisivel == 3 else 'nao')