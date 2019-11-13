#dizi üzerinde yýgýn

yigin=[]

def bilgiat(n):
    global yigin
    yigin.append(n)

def bilgicek():
    global yigin
    if len(yigin)==0:
        print("yigin zaten bos")
    else:
        print(yigin[len(yigin)-1])
        yigin=yigin[0:len(yigin)-1]
