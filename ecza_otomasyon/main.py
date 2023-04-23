import database, os
from time import sleep
from winsound import Beep

class Kutuphane:
    def __init__(self, adi):
        self.adi = adi
        self.durum = True

        database.baglanti() 
        
    def calistir(self):
        self.menu()
    
    def menu(self):
        os.system("cls")
        print("""-------- {} Eczane Otomasyon Sistemi --------     
        1- İlaç Ekle
        2- İlaç Sil
        3- İlaç Güncelle
        4- İlaç Listele
        5- Çıkış""".format(self.adi))
        secim = self.secim()

        if secim == 1:
            self.ilacEkle()
        
        if secim == 2:
            self.ilacSil()
        
        if secim == 3:
            self.ilacGuncelle()
        
        if secim == 4:
            self.ilacListele()
        
        if secim == 5:
            self.cikis()
        
        
    def secim (self):
        while True:
            try:
                seciminiz = int(input("1-5 Arası Seciminizi Yapın.: "))
                if seciminiz < 1 or seciminiz > 5:
                    Beep(2500, 1000)
                    print("\a1-5 arası değer girmelisiniz!\a")
                    continue   # dongunun başına dön
                break
            except ValueError:
                print("Metinsel İfade Girilemez!\t1-5 arası değer girin")
        return seciminiz
    
    def ilacEkle(self):
        print(" ilac Ekle Menüsü ".center(30, "*"))
        self.ad = input("ilac Adı Girin.: ").lower().capitalize()
        self.uretici = input("uretici Adı Girin.: ").lower().capitalize()
        self.turu = input("Turunu Girin.: ").lower().capitalize()
        self.fiyat = int(input("Fiyatını Girin.: "))
        
        while True:
            try:
                self.stoktaMi = int(input("Stokta İse 1 - Yoksa Sıfır 0..: "))
                if self.stoktaMi < 0 or self.stoktaMi > 1:
                    print("1 veya 0 degerlerini girin!")
                    continue
                break
            except ValueError:
                print("0 veya 1 girin")
        
        database.ekle()
        sleep(2)
        print("ilac Başarıyla Veritabanına Eklendi")    
        sleep(5)
            
    def ilacSil(self):
        os.system("cls")
        print(" ilac Silme Menusu ".center(30, "*"))
        database.sil()
        sleep(2)
        print("\nilac Başarılı Şekilde Silinmiştir.")
        sleep(5)
            
    def ilacGuncelle(self):
        os.system("cls")
        print(" ilac Guncelle Menusu ".center(30, "*"))
        database.guncelle()
        sleep(2)
        print("\nilac Başarılı Şekilde Guncellenmistir.")
        sleep(5)
    
    def ilacListele(self):
        os.system("cls")
        print(" ilac Listeleme Menusu ".center(30, "*"))
        database.listele()
        sleep(5)
    
    def cikis(self):
        self.durum = False
    
k = input("Eczane Adını Giriniz..: ")
kutuphane1 = Kutuphane(k)

while kutuphane1.durum:
    kutuphane1.calistir()