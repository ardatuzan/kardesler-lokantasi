print("""****************************************
Kardeşler Lokantasına Hoş Geldiniz   :)
****************************************""")
isim = input("""              Selamlar!
 Ben Çınar Burada Bulunduğunuz Süre Boyunca Size Ben Yardımcı Olacağım :)
         Öncelikle İsminizi Öğrenebilir Miyim? """)

siparis = input(isim+" " """Ha Çok Güzel Bir İsim. 
     Şefimiz Bugün 
     Kahvaltı, Çorba ve Ana Yemek Türlerinde 
     Nefiss Yemekler Çıkardı Ne Tür Bir Yemek İstersin"""+ " "+isim+"""?
     """)
urun = 0
parabirimi = "TL"
fiyat = 0
porsiyon = 0
if siparis == "Kahvaltı":
 urun = int(input("""*KAHVALTILIKLAR*
1)Sosis Ağırlıklı Serpme Kahvaltı --> 520 TL
2)Sucuk Ağırlıklı Serpme Kahvaltı --> 560 TL 
Kaç Numaralı Ürünümüzü İstersiniz Efendim?"""))

elif siparis == "Çorba":
 urun = int(input("""*ÇORBA ÇEŞİTLERİ*
3)Mercimek --> 60 TL
4)Kelle Paça --> 150 TL
5)Ayak Paça --> 190 TL
6)İşkembe --> 80 TL
7)Tandır --> 70 TL
Kaç Numaralı Ürünümüzü İstersiniz Efendim? """))

elif siparis == "Ana Yemek":
 urun = int(input("""*YEMEKLER* 
8)Afyon Kebap --> 200 TL
9)Adana Kebap --> 220 TL
10)Urfa Kebap --> 210 TL
11)Beyti Kebap --> 250 TL
12)Taze Fasulye --> 100 TL
13)Kuru Fasulye --> 150 TL
14)Tandır Et --> 260 TL
15)Pilav --> 50 TL
Kaç Numaralı Ürünümüzü İstersiniz Efendim?"""))

if urun == 1:
    fiyat = 520

elif urun == 2:
    fiyat = 560

elif urun == 3:
    fiyat = 60

elif urun == 4:
    fiyat = 150

elif urun == 5:
    fiyat = 190

elif urun == 6:
    fiyat = 80

elif urun == 7:
    fiyat = 70

elif urun == 8:
    fiyat = 200

elif urun == 9:
    fiyat = 220

elif urun == 10:
    fiyat = 210

elif urun == 11:
    fiyat = 250

elif urun == 12:
    fiyat = 100

elif urun == 13:
    fiyat = 150

elif urun == 14:
    fiyat = 260

elif urun == 15:
    fiyat = 50

if 1 <= urun <= 15:
 porsiyon = int(input("Harika! Kaç Porsiyon İstersiniz?"))

 hesap = fiyat * porsiyon

 print("Toplam Ücretiniz =",hesap,parabirimi )

else:
    print("Maalesef Şefimiz Bugün O Tür Bir Yemek Yapmadı")