def anaMenu():
    print("ÜLKE BASKENT VERİ TABANI")
    print("-----------------------")
    print("1. Kayıt Ekleme")
    print("2. Kayıt Silme")
    print("3. Sözlügü ekrana yazdırma")
    print("4. Ülkenin baskentini arama")
    print("5. Baskentin ait oldugu ükeyi arama")
    print("6. Tüm sözlügü silme")
    print("7. Cıkıs")
    print("------------------------")
    secim=int(input("Seciminiz (1-7) : "))
    return secim

# Sözlüge yeni kayıt ekleme (Ülke:baskent)
def kayitEkle(s):
    ulke=''
    while ulke!='*':
        ulke=input("Ülke ismini giriniz (Çıkmak icin *) ")
        if ulke!='*':
            if ulke in s.keys():
                print("Bu ülkenin baskenti ",s[ulke]," olarak girilmistir.")
                t=input("Degistirmek istiyor musunuz (degistirmek icin 'e') ")
                if t=='e' or t=='E':
                    baskent=input("Yeni baskenti giriniz :")
                    s[ulke]=baskent # Sözlükte güncelleme
            else:
                baskent=input("Baskenti giriniz: ")
                s[ulke]=baskent # Yeni kayıt ekleme

#Sözlükten bir kayıt silen fonksiyon
def kayitSilme(s):
    ulke=input('Silinecek ülkeyi giriniz: ')
    if ulke in s.keys():  # ülke gercekten anahtarların ıcındeyse
        b = s[ulke]  # silinecek ülkenın (anahtarın) ismi
        del s[ulke]  # kayıt silme islemi
        print(ulke," ve baskenti ",b," sozlukten silindi")
    else:
        print(ulke," sözlükte kayıtlı degıl islem yapılamadı")
        
# Sözlükten ekrana yazdıran fonksiyon
def ekranaYazdir(s):
    i=1
    print("SOZLUKTE KAYIRLI ULKE VE BASKENTLER")
    print("-----------------------------------")
    for ulke,baskent in s.items():
        print(i,". ",ulke," ---> ",baskent)
        i=i+1

# Girilen ülkenin baskentini ekrana yazdıran fonksiyon
def baskentArama(s):
    ulke=''
    while ulke!='*':
        ulke=input("Ülke ismini giriniz (Cıkmak ıcın *) ")
        if ulke!='*':
            if ulke in s.keys():
                print(ulke, "'nin baskenti ",s[ulke]," dir")
            else:
                print(ulke, " sözlüktekte kayıtlı degıl!")



# Girilen baskentin ait oldugu ülkeyi ekrana yazdıran fonksiyon
def ulkeArama(s):
    baskent=''
    while baskent!='*':
        baskent=input("Baskenti giriniz (cıkmak icin *) ")
        if baskent!='*':
            bulundu=False
            for k,v in s.items():
                if v==baskent:
                    print(baskent," ",k," nin baskentidir.")
                    bulundu=True
            if (bulundu==False):
                print("Bu baskent sözlüktekte kayıtlı degıl!")

  

#ANA PROGRAM
sozluk={}  # Bos sozluk
secim=0
while secim!=7:   #islemin secilmedigi surece
    secim=anaMenu()
    if secim==1:
        kayitEkle(sozluk)
    elif secim==2:
        kayitSilme(sozluk)
    elif secim==3:
        ekranaYazdir(sozluk)
    elif secim==4:
        baskentArama(sozluk)
    elif secim==5:
        ulkeArama(sozluk)
    elif secim==6:
        t=input("Emin misiniz (Silmek icin 'e') :")
        if t=="e" or t=="E":
            sozluk.clear()
    elif secim==7:
        print("Program sonlandı. Güle Güle!")
    else:
        print("Pardon ??")
        
