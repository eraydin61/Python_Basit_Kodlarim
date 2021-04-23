# ( Bubble Sort ) - KABARCIK SIRALAMA - ALGORITMASI

import random

def bubbleSort(liste):
    boy=len(liste)
    for tur in range(boy-1):
        for i in range(boy-1):
            if liste[i]>liste[i+1]:  # iki eleman yer degıstırmeli
                t=liste[i]
                liste[i]=liste[i+1]
                liste[i+1]=t

#ANA PROGRAM
a=[]
for i in range(50):
    a.append(random.randint(10,200))

print("Listenin İlk Durumu :")
print(a)

bubbleSort(a)

print()
print("Listenin Son Durumu")
print(a)
            
