
def converterHexa(numero):
    if(numero == '0000'): return '0'
    if(numero == '0001'): return '1'
    if(numero == '0010'): return '2'
    if(numero == '0011'): return '3'
    if(numero == '0100'): return '4'
    if(numero == '0101'): return '5'
    if(numero == '0110'): return '6'
    if(numero == '0111'): return '7'
    if(numero == '1000'): return '8'
    if(numero == '1001'): return '9'
    if(numero == '1010'): return 'A'
    if(numero == '1011'): return 'B'
    if(numero == '1100'): return 'C'
    if(numero == '1101'): return 'D'
    if(numero == '1110'): return 'E'
    if(numero == '1111'): return 'F'

codigoErro = str(input())

parte1 = '0x' + converterHexa(codigoErro[:4]) + converterHexa(codigoErro[4:8])
parte2 = '0x' + converterHexa(codigoErro[8:12]) + converterHexa(codigoErro[12:])
codigoConvertido = parte1 + ' ' + parte2
print(codigoConvertido)
    