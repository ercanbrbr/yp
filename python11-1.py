import random
def ran(n):
    #random.seed(100)
    a=[]
    for i in range(n):
        a.append(random.randint(-0,100))
    return a
def mean(dizi):
    ortalama=0
    for i in dizi:
        ortalama+=i
    ortalama=ortalama/len(dizi)
    return ortalama
def ss(dizi):
    ort=mean(dizi)
    std=0
    for i in dizi:
        std=std+(i-ort)**2
    std=(std/(len(dizi)-1))**0.5
    return std
def normalize(dizi):
    a=[]
    ort=mean(dizi)
    std=ss(dizi)
    for i in range(len(dizi)):
        a.append((dizi[i]-ort)/std)
    return a
def getmean(dizi):
    kactane=0
    toplamadet=0

    ortalama=mean(dizi)
    standarts=ss(dizi)

    low=ortalama-standarts
    high=ortalama+standarts

    for x in dizi:
        toplamadet=toplamadet+1
        if(x>low and x<high):
            kactane=kactane+1
    return kactane/toplamadet
def insertionsort(dizi):
    sayilar2=[]
    for i in dizi:
        sayilar2.append(i)
    kar=0
    swap=0
    for i in range(1,len(dizi)):
        for j in range(i,0,-1):
            kar+=1
            if sayilar2[j]<sayilar2[j-1]:
                swap+=1
                #swap
                temp=sayilar2[j-1]
                sayilar2[j-1]=sayilar2[j]
                sayilar2[j]=temp

    return sayilar2,swap,kar
def bubble(dizi):
    sayilar2=[]
    for i in dizi:
        sayilar2.append(i)
    n=len(dizi)
    kar=0
    swap=0
    for i in range(n):
        for j in range(0,n-i-1):
            kar+=1
            if sayilar2[j] > sayilar2[j+1]:
                swap+=1
                sayilar2[j], sayilar2[j+1] = sayilar2[j+1], sayilar2[j]
    return sayilar2,swap, kar
def shellsort(dizi):
    return 0
def ortswapkar(deneme):
    swapinsert=[]
    swapbubble=[]
    for i in range(deneme):
        d1=ran(10)
        s1=insertionsort(d1)
        s2=bubble(d1)
        swap1=s1[1]
        swap2=s2[1]
        swapinsert.append(swap1)
        swapbubble.append(swap2)
    ortswapinsert=mean(swapinsert)
    stdswapinsert=ss(swapinsert)
    ortswapbubble=mean(swapbubble)
    stdswapbubble=ss(swapbubble)
    return ortswapinsert,stdswapinsert,ortswapbubble,stdswapbubble

print(ortswapkar(100))





def bos():
    '''dizi=ran(5)
    print("Dizi..: ",dizi)
    ort=mean(dizi)
    print("Ortalama..: ",ort)
    standart=ss(dizi)
    print("Standart Sapma..: ",standart)
    norma=normalize(dizi)
    print("Normalize Edilmiş..: ",norma)
    print("Yeni Sayıların Standart Sapması..: ",ss(norma))
    dizi2=ran(100)
    print(getmean(dizi2))

    dizi3=ran(5)
    print(dizi3)
    print("---------------------")'''
