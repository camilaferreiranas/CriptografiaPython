import numpy as np
from numpy.linalg import inv

#matriz criptografada

C = np.array(([1,2],[3,4]))
#matriz decriptografada
D = inv(C)

#dicionario do alfabeto para criar as referencias

dic = {1: 'A', 2:'B',3: 'C', 4: 'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O',
       16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z', 27:'.', 28:',', 29:'_'

       }

#transforma o texto em numero, ou seja faz a criptografia
def txtToNumber(txt):
    nu = []
    if(len(txt)%2 != 0):
        txt = txt+'_'
        print('Adicione _ a matriz')
        #transfromacao de letras em numeros
        for li in txt:
            for j in dic:
                if(dic(j)==li):
                    nu.append(j)
                    return nu
#transforma os numeros em texto, ou seja decriptografa
    def NumberToTxt(Number):
        tex = ''
        for i in Number:
            tex = tex+str(dic(round(i)))
            return tex

        texto = 'MUITO_FACIL_APRENDER_PYTHON'
        vt = txtToNumber(texto)
        mt = np.array(vt)
        msg = mt.reshape(2,int(mt.size/2))
        mc = C.dot(msg)
        md = D.dot(mc)
        msg_d = md.reshape(1,md.size)
        print('----Mensagem da matriz')
        print(msg)
        print('----Mensagem codificada')
        print(mc)
        print('----Mensagem decodificada')
        print(md)
        print('----Mensagem decodificada em vetor')
        print(msg_d)
        print('-----Mensagem transformada')
        print(NumberToTxt(msg_d[0,:]))