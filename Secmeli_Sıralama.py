#Selection Sort Sıralam Algorıtması  (SECMELİ SIRALAMA)

import random

def EnKüçükElemanıTası(liste,a,b):
    ek=liste[a]
    yer=a
    for j in range(a+1,b+1):
        if liste[j]<ek:
            ek=liste[j]
            yer=j
        #en kücük elemanı en basa tasıma
    if yer!=a: # eger en kucuk eleman en basta degılse
        t=liste[a]
        liste[a]=liste[yer]
        liste[yer]=t

#ANA PROGRAM
x=[]
for i in range(50):
    x.append(random.randint(10,300))

print("Listenin İlk Durumu :")
print(x)

boy=len(x)
for a in range(0,boy-1):
    EnKüçükElemanıTası(x,a,boy-1)

print()
print("Listenin Son Durumu")
print(x)
