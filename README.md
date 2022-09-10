# Akbank Web3 Practicum


 **Yapılması İstenen:** Boğaz köprülerinden geçiş yapan araçlardaki HGS cihazlarının yazılımını yazmanızı bekliyoruz. Buna göre araçların HGS kayıtlarının tutulması sırasında bir HGS numarası, sahibinin ismi ve soyismi, aracın sınıfı (1. Sınıf: otomobil, 2. Sınıf: minibüs, 3. Sınıf: otobüs), geçiş yaptığı tarih ve saat bilgileri, bakiyesi gibi bilgileri tutacak ve aşağıdaki istenenleri karşılayacaksınız.

 - Her araç sınıfı için ayrı bir sınıf (class) tanımı yapınız.
 - Ödeme kabul eden fonksiyonu olan bir gişe sınıfı ekleyiniz. Bu fonksiyon, bütün araç sınıflarını kabul eden ve ilgili araç sınıfına göre bakiyeyi azaltan tek bir fonksiyon olsun.
    
- OGS yönetimi için raporlama yapmanız isteniyor. Gişe sınıfının, günlük olarak geçen araçları bir dizide (array) tutmasını sağlayınız. Yönetim için yeni bir sınıf yazıp, istenildiğinde elde edilen toplam günlük bakiyeyi ekrana basan bir fonksiyon yazınız.


---------------------------
**Yapılanlar:** Araç bilgilerini ***(Ad, Soyad, Tarih, Bakiye, Araç Sınıfı)*** tutmak için bir HGS sınıfı tanımlandı. HGS sınıfından 3 farklı ***(Otomobil, Minibus, Otobüs)***  araç sınıfı kalıtım yolu ile türetildi.

Araçların giriş/çıkış saatlerini ve bakiyelerini kontrol eden gişe sınıfı tanımlandı. Bu sınıf içerisinde tanımlı olan *odemeYapma()* fonksiyonuna verilen araç nesneleri ve tarih bilgileri ile araçların giriş/çıkış yapmaları kontrol edildi ve array içerisinde saklandı.

Array içerisinde saklanan bilgileri ve toplam bakiyeyi döndürmek için *Yönetim* sınıfı tanımlandı.


-----
*Kullanılan dil:* Python


