class Araba:  #araba sinifi olusturuldu 
    def __init__(self, marka, model):#self nesneine 2 tane parametere atandi 
        self.marka = marka
        self.model = model

    def bilgileri_yazdir(self):#bu fonksiyon nesneyi ekrana yazdirdi
        print(f"Marka: {self.marka}, Model: {self.model}")

# Kullanım
araba1 = Araba("Toyota", "Corolla")#raba sınıfından araba1 adında bir nesne oluşturuyorsun.
araba1.bilgileri_yazdir()#ekrana yazdirdi



#\-----------------------------------------------------------------------------------------------------\

class Dikdortgen:#Dikdortgen sınıfını tanımlıyorsun
    def __init__(self, genislik, yukseklik):#Nesne oluşturulurken genislik ve yukseklik değerlerini alıp kaydediyor.
        self.genislik = genislik
        self.yukseklik = yukseklik

    def alan_hesapla(self):#Dikdörtgenin alanını (genişlik * yükseklik) hesaplayıp döndürüyor.
        return self.genislik * self.yukseklik

# Kullanım
dikdortgen1 = Dikdortgen(5, 10)#5 genişlik, 10 yükseklik ile bir dikdörtgen nesnesi oluşturuluyor.
alan = dikdortgen1.alan_hesapla()#alan hesaplatiliuor
print(f"Dikdörtgenin alanı: {alan}")#ekrana yazdir


#\-----------------------------------------------------------------------------------------------------\

class Kare:#kare sinifi
    def __init__(self, kenar):#kenarini alip kaydetti
        self.kenar = kenar

    def kareyi_yazdir(self):#sekli cizzen fonkssiyon 
        for i in range(self.kenar):#for dongusu yardim etti cizmeye
            print("* " * self.kenar)

# Kare sınıfından bir nesne oluşturma ve kareyi yazdırma
kare1 = Kare(5)#kenar uzunlugu 5
kare1.kareyi_yazdir()#ekrana yzdirdik


#\-----------------------------------------------------------------------------------------------------\


class HesapMakinesi:
    def topla(self, sayi1, sayi2, sayi3=None):#bu fonksiyon 3. sayi girilmedigi takdirde iki sayi toplamini girilirse 3 sayi toplamini verir
        if sayi3 is not None:
            return sayi1 + sayi2 + sayi3
        else:
            return sayi1 + sayi2

# HesapMakinesi sınıfından bir nesne oluşturma
hesap_makinesi = HesapMakinesi()

# İki sayı ile toplama
sonuc1 = hesap_makinesi.topla(10, 20)
print("İki sayının toplamı:", sonuc1)

# Üç sayı ile toplama
sonuc2 = hesap_makinesi.topla(10, 20, 30)
print("Üç sayının toplamı:", sonuc2)

#\-----------------------------------------------------------------------------------------------------\





class Merhaba:
    def merhaba_yazdir(self):
        print("Merhaba Dünya")

# Merhaba sınıfından bir nesne oluşturma ve metodu çağırma islemi yapildi
merhaba = Merhaba()
merhaba.merhaba_yazdir()


#\-----------------------------------------------------------------------------------------------------\


# İnsan sınıfı
class Insan:#insan sinif tanimlandi
    def __init__(self, ad, yas):#ad ve yas degerleri kaydedilir
        self.ad = ad
        self.yas = yas

    def konus(self):#konusmayi sagkayan fonksiyon
        print(f"Merhaba, ben {self.ad}, {self.yas} yaşındayım.")


# Hoca sınıfı (miras alma - inheritance)
class Hoca(Insan):#insan snifindan dalladi
    def __init__(self, ad, yas, sicil_no):
        super().__init__(ad, yas)   # Insan sınıfının özelliklerini miras al
        self.sicil_no = sicil_no

    # konus metodunu ezme (override)
    def konus(self):
        print(f"Benim adım {self.ad}, {self.yas} yaşındayım ve öğretmenim.")

    def ders_ver(self):
        print(f"Hoca {self.ad} ders veriyor. (Sicil No: {self.sicil_no})")


# Kullanım
insan1 = Insan("Ahmet", 30)
insan1.konus()

hoca1 = Hoca("Mehmet", 45, "H1234")
hoca1.konus()       # override edilmiş versiyon çalışacak
hoca1.ders_ver()
