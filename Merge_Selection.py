import random
import time
# a ve b küçükten buyuge sıralı listeler
# fonksiyon geriye tek bir büyükten kucuge sıralı lıste cıkarıyor
def birlestir(a,b):
    c=[]
    while len(a)>0 and len(b)>0:  # her iki listede eleman oldugu surece
        if a[0]<b[0]: # eğer a[0] < b[0] dan 
            c.append(a[0]) # a[0] ı c ye ekle
            a=a[1:]   # a listesindeki ilk eleman kırpılır
        else:
            c.append(b[0])
            b=b[1:]
    if len(a)>0:  # a listesinde eleman kalmış ise
        c.extend(a) # a daki elemanları c ye ekliyor 
    if len(b)>0:  # b listesinde eleman kalmaş ise
        c.extend(b)
    return c # c listesini geri döndür 
def mergeSort(x):
    if len(x)==1:
        return x
    orta=len(x)//2 
    sol=x[:orta]  # baştan ortaya kadar
    sag=x[orta:]  # ortadan sona kadar
    sol=mergeSort(sol)  # solu tekrar fonksiyona yollayıp tekrar ikiye böldürüyor
    sag=mergeSort(sag)  # sağı tekrar fonksiyona yollayıp tekrar ikiye böldürüyor
    sonuc=birlestir(sol,sag) # birleşire sol ve sağı yolluyoruz
    return sonuc # sonucu geri döndür



a=[]
print("Liste olusturuluyor...")
# 10.000 elemanlı 1 ile 10.000 sayıları arasında liste oluşturma
for i in range(10):
    a.append(random.randint(1,10000))

print("------------------------------")
print("Liste siralaniyor... (Merge Sort")
baslangıc2_zaman=time.time()
a=mergeSort(a)     # Merge çözüm fonksiyonunu çağırma
bitis2_zaman=time.time()
print("Siralama tamamlandi! (Merge Sort)")
print("Geçen süre:(Merge)   ",bitis2_zaman-baslangıc2_zaman,"   Saniyedir.")
print(a)
