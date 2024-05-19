def eNumero(numero):
    numeros = '1234567890'
    for x in numero:
        if x not in numeros:
            return False
    return True

def eLetra(palavra):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for x in palavra:
        if x not in letras:
            return False
    return True

placa = input().upper()

if placa == '':
    print('Placa invalida')
elif eLetra(placa):
    print('Placa invalida')
elif len(placa) > 7:   
    print('Placa invalida')
elif eLetra(placa[:3]) and eNumero(placa[3]) and eLetra(placa[4]) and eNumero(placa[5:]):
    print('Placa Mercosul')
elif eNumero(placa):
        print('Placa numerica')
elif(len(placa) == 7): # 1941 a 1969
    if(eNumero(placa[3:]) and eLetra(placa[:3])):# 1990 a 2018
        print('Placa AAA-9999')
    else:
        print('Placa invalida')
elif(eLetra(placa[:2]) and eNumero(placa[2:]) and len(placa) == 6): # 1970 a 1990
    print('Placa AA-9999')
elif(eLetra(placa[0]) and eNumero(placa[1:]) and len(placa) >= 2 and (placa[0] == 'A' or placa[0] == 'P')): # 1915 a 1941
    print('Placa muito antiga')
else:
    print('Placa invalida')