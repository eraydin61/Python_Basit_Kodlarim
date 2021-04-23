# Sifre Tablosu
import random

def sifreTablosuOlustur():
    t={}
    for i in range(65,91):
        anahtar=chr(i)
        deger=chr(random.randint(65,90))
        # Üretilen değer daha once sözlüğe eklendiyse
        # yeni bir harf üretilmelidir.
        while deger in t.values():
            deger=chr(random.randint(65,90))
        t[anahtar]=deger
    return t

# t Sifre tablosunu kullanarak m metnini Sifreleyen
# ve sonucu geri döndüren fonksiyon
def sifrele(t,m):
    sifrelenmisMetin=''
    for i in range(len(m)):
        if m[i] in t.keys():
            sifrelenmisMetin = sifrelenmisMetin + t[m[i]]
        elif m[i]==" ":
            sifrelenmisMetin = sifrelenmisMetin + " "
        else:
            sifrelenmisMetin = sifrelenmisMetin + "?"
    return sifrelenmisMetin

# t Sifre tablosunu kullanarak c Sifreli metnini cözen
# ve düz metni geri döndüren fonksiyon
def sifreCoz(t,c):
    duzMetin=''
    for i in range(len(c)):
        if c[i]==" ":  # Sifreli harf bosluk ise
            duzMetin = duzMetin + " "
        else: # Sifreli harfi sözlükte ara
            bulundu=False
            for a,d in t.items():
                if c[i]==d:
                    duzMetin = duzMetin + a
                    bulundu=True
            if bulundu==False:
                duzMetin = duzMetin + "?"
    return duzMetin

def tabloyuYazdir(t):
    for a,d in sorted(t.items()):
        print(a," --> ",d)

#Ana Program
tablo=sifreTablosuOlustur()
tabloyuYazdir(tablo)
p=input("Sifrelenecek metni giriniz (A-Z harfleri ile) : ")
c=sifrele(tablo, p)
print("Sifreli karakter : ",c)

c=input("Desifre edilecek metni giriniz (A-Z harfleri ile) : ")
m=sifreCoz(tablo, c)
print("Düz metin karakter : ",m)
