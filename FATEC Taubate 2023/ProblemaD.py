deu_erro = False
num = str(input()).strip()
x = len(num)

if(x > 15 or x < 15):
    pass
else:
    for i in num:            
        if(i != 0 or i != 1 or i != 9 or i != ' '):
            tem_pontuacao = True
            
        if(tem_pontuacao == True):
            pass
    else:
        for i in num:
            if(i == '0' or i == '1' or i == ' '):
                pass
            else:
                deu_erro = True

        if(deu_erro == True):
            print('F')
        else:
            print('S')