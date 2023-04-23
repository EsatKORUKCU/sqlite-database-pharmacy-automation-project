import sqlite3, main

def baglanti():   # tablo ve database oluşturulur
    with sqlite3.connect("ilacdepo.db") as baglan:
        imlec = baglan.cursor()
        imlec.execute(""" create table if not exists eczane(
                adi TEXT,
                firma TEXT,
                turu TEXT,
                fiyat FLOAT,
                stoktaMi BOOL
            ) """)
        baglan.commit()
        
def ekle():
    with sqlite3.connect("ilacdepo.db") as baglan:
        imlec = baglan.cursor()
        imlec.execute(""" insert into eczane values ("{}","{}","{}","{}","{}") """.format(
            main.kutuphane1.ad,
            main.kutuphane1.uretici,
            main.kutuphane1.turu,
            main.kutuphane1.fiyat,
            main.kutuphane1.stoktaMi
        ))
        baglan.commit()

def listele():
    with sqlite3.connect("ilacdepo.db") as baglan:
        imlec = baglan.cursor()
        imlec.execute(""" select * from eczane """)
        ilaclar = imlec.fetchall()
        metineCevir = lambda arguman : [str (y) for y in arguman]
        for sayi, eleman in enumerate(ilaclar, 1):
            print("{}- {}".format(sayi, "".join(metineCevir(eleman))))
        baglan.commit()

def sil():
    listele()
    with sqlite3.connect("ilacdepo.db") as baglan:
        imlec = baglan.cursor()
        while True:
            try:
                secim = int(input("Silinecek İlac No Girin.: "))
                break
            except Exception:
                print("Gecersiz Deger Girdiniz.")
            
        imlec.execute(f""" delete from eczane where rowid={secim} """)
        baglan.commit()

def guncelle():
    listele()
    with sqlite3.connect("ilacdepo.db") as baglan:
        imlec = baglan.cursor()
        while True:
            try:
                secim = int(input("Guncellenecek İlac No Girin.: "))
                break
            except Exception:
                print("Gecersiz Deger Girdiniz.")
        
        while True:
            try:
                guncelleSecim = int(input(""" Guncellenecek Alan Adını Seçin
    1- ADI
    2- URETICI FIRMA
    3- TURU
    4- FIYAT
    5- STOK DURUMU

Seciminiz.......: """))
                if guncelleSecim < 1 or guncelleSecim > 5:
                    break
            except Exception:
                print("Sayisal Bir Değer Giriniz")
            alanAdlari = ["adi", "firma", "turu", "fiyat", "stoktaMi"]
            yeniDeger = input("Yeni Değer Girin..: ")
            
            imlec.execute(""" update eczane set {} = "{}" where rowid={} """.format(alanAdlari[guncelleSecim -1], yeniDeger, secim))
            baglan.commit()
            break   