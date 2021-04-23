# Caesar Şifreleme / Şifre çözme Programı
# 21.11.2017, ders uygulaması

# Verilen mesajı Şifreleyen fonksiyon
def sifrele(mesaj):
    sifrelimesaj=""
    boy=len(mesaj)
    for i in range(boy):  #mesajdaki her harf için
        kod=ord(mesaj[i])
        kod=kod+3
        if kod>90:   # X,Y,Z harfleri için A,B,C olmali
            kod=kod-26
        sifreliharf = chr(kod)
        if (mesaj[i]!=" "):
            sifrelimesaj=sifrelimesaj+sifreliharf
        else:
            sifrelimesaj=sifrelimesaj+" "

    return sifrelimesaj


# Verilen Şifreli Mesajı Çözen fonksiyon
def sifreCoz(smesaj):
    duzmesaj=""
    boy=len(smesaj)
    for i in range(boy):  #mesajdaki her harf için
        kod=ord(smesaj[i])
        kod=kod-3
        if kod<65:   # A,B,C harfleri için X,Y,Z olmalı
            kod=kod+26
        duzharf = chr(kod)
        if (smesaj[i]!=" "):
            duzmesaj=duzmesaj+duzharf
        else:
            duzmesaj=duzmesaj+" "

    return duzmesaj

### ANA PROGRAM
m=input("Mesajınız: ")
c=sifrele(m)
print("Mesajınızın Sifreli Kodu :",c)

m=input("sifreli Mesajı girin: ")
c=sifreCoz(m)
print("Mesajınız :",c)
