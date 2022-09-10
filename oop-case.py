import datetime as date,datetime
import time

#Araç bilgilerinin tutulduğu sınıf
class HGS_KAYITLARI:
    def __init__(self, HGS_NO, _aracSahibiAdi, _aracSahibiSoyadi, _aracSinifi ,_gecisYaptigiTarih, _bakiye):
        self.hgs_no = HGS_NO
        self.aracSahibiAdi = _aracSahibiAdi
        self.aracSahibiSoyadi = _aracSahibiSoyadi
        self.aracSinifi = _aracSinifi
        self.gecisYaptigiTarih = _gecisYaptigiTarih
        self.bakiye = _bakiye
    
    def aracBilgileriDondur(self):
        return("HGS NO: " + str(self.hgs_no), 
               "ARAC SAHİBİ ADİ:" + str(self.aracSahibiAdi), 
               "ARAC SAHİBİ SOYADI:"+ str(self.aracSahibiSoyadi), 
               "ARAC SINIFI:" + str(self.aracSinifi),
               "TARİH:"+ str(self.gecisYaptigiTarih),
               "BAKİYE:"+  str(self.bakiye))
        
        
#HGS sınıfı üzerinden kalıtılan araç sınıfları
class Otomobil(HGS_KAYITLARI):
    def __init__(self, HGS_NO, _aracSahibiAdi, _aracSahibiSoyadi ,_gecisYaptigiTarih , _bakiye):
        self.aracSinifi = "Otomobil"
        super(Otomobil, self).__init__( HGS_NO, _aracSahibiAdi, _aracSahibiSoyadi, self.aracSinifi ,_gecisYaptigiTarih , _bakiye)
        
        
class Minibus(HGS_KAYITLARI):
    def __init__(self, HGS_NO, _aracSahibiAdi, _aracSahibiSoyadi ,_gecisYaptigiTarih , _bakiye):
        self.aracSinifi = "Minibus"
        super(Minibus, self).__init__( HGS_NO, _aracSahibiAdi, _aracSahibiSoyadi, self.aracSinifi ,_gecisYaptigiTarih , _bakiye)

class Otobus(HGS_KAYITLARI):
    def __init__(self, HGS_NO, _aracSahibiAdi, _aracSahibiSoyadi ,_gecisYaptigiTarih , _bakiye):
        self.aracSinifi = "Otobus"
        super(Otobus, self).__init__( HGS_NO, _aracSahibiAdi, _aracSahibiSoyadi, self.aracSinifi ,_gecisYaptigiTarih , _bakiye)
        

#Araçların bakiyelerini sınıflarına göze azaltan ve giriş/çıkış tarihlerini kayıt eden sınıf
class Gise():
    def __init__(self):
        self.toplamBakiye = 0
        self.gecenAracListesi = list()

    def odemeYapma(self, arac, _gecisYaptigiTarih):
        self.aracSinifi = arac.aracSinifi
        
        if(self.aracSinifi == "Otomobil" and arac.bakiye >= 50):
            arac.bakiye -= 50
            self.toplamBakiye += 50
            arac.gecisYaptigiTarih = _gecisYaptigiTarih
            self.gecenAracListesi.append(arac.aracBilgileriDondur())
            
        elif(self.aracSinifi == "Minibus" and arac.bakiye >= 60):
            arac.bakiye -= 60
            self.toplamBakiye += 60
            arac.gecisYaptigiTarih = _gecisYaptigiTarih
            self.gecenAracListesi.append(arac.aracBilgileriDondur())
            
        elif(self.aracSinifi == "Otobus" and arac.bakiye >= 65):
            arac.bakiye -= 65
            self.toplamBakiye += 65
            arac.gecisYaptigiTarih = _gecisYaptigiTarih
            self.gecenAracListesi.append(arac.aracBilgileriDondur())
        
        
        
#Kayıt edilen araçlara ait bilgileri döndüren ve toplam bakiyeyi tutan sınıf.
class Yonetim():
    def __init__(self, giseIslemleri):
        self.bakiye = giseIslemleri.toplamBakiye
        self.gecenAraclar = giseIslemleri.gecenAracListesi
        
    def toplamBakiye(self):
        print("Toplam Bakiye:" + str(self.bakiye) + "TL")
        
    def gecenAracListesi(self):
        for i in range(len(self.gecenAraclar)):
            print(self.gecenAraclar[i])
            print("\n")
            
        
    

#Otomobil nesnelerinin tanımlanması
arac1 = Otomobil(101,"Muhammed","Altunisik",0,500)
arac2 = Otomobil(102,"Furkan","Öztürk",0,700)
arac3 = Minibus(103,"Hasan","Güray",0,400)
arac4 = Minibus(104,"Erim","Şahin",0,200)
arac5 = Otobus(105,"Fırat","Sandıkçı",0,65)
arac6 = Otobus(106,"Ahmet","Karahan",0,105)
arac7 = Otomobil(107,"Mahmut","Tuncer",0,100)

#Gise sınıfının tanımlanması ve Gise sinifinda ki odemeYapma fonksiyonun her araç için ayrı ayrı çağrılması
gise = Gise()
gise.odemeYapma(arac1, datetime.datetime.strftime(date.datetime.now(), '%c'))
gise.odemeYapma(arac2, datetime.datetime.strftime(date.datetime.now(), '%c'))
gise.odemeYapma(arac3, datetime.datetime.strftime(date.datetime.now(), '%c'))
gise.odemeYapma(arac4, datetime.datetime.strftime(date.datetime.now(), '%c'))
gise.odemeYapma(arac5, datetime.datetime.strftime(date.datetime.now(), '%c'))
gise.odemeYapma(arac6, datetime.datetime.strftime(date.datetime.now(), '%c'))
gise.odemeYapma(arac7, datetime.datetime.strftime(date.datetime.now(), '%c'))


#Yonetim sınıfının tanımlanması ve kayıtlı olan bilgilerin kullanıcıya gösterilmesi
yonetim = Yonetim(gise)
yonetim.gecenAracListesi()
yonetim.toplamBakiye()