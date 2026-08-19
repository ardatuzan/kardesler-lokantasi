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

if siparis == "Kahvaltı":
 urun = int(input("""*KAHVALTILIKLAR*
1)Sosis Ağırlıklı Serpme Kahvaltı
2)Sucuk Ağırlıklı Serpme Kahvaltı
Kaç Numaralı Ürünümüzü İstersiniz Efendim?"""))

elif siparis == "Çorba":
 urun = int(input("""*ÇORBA ÇEŞİTLERİ*
3)Mercimek
4)Kelle Paça
5)Ayak Paça
6)İşkembe
7)Tandır
Kaç Numaralı Ürünümüzü İstersiniz Efendim? """))

elif siparis == "Ana Yemek":
 urun = int(input("""*YEMEKLER* 
8)Afyon Kebap
9)Adana Kebap
10)Urfa Kebap
11)Beyti Kebap
12)Taze Fasulyegit
13)Kuru Fasulye
14)Tandır Et
15)Pilav
Kaç Numaralı Ürünümüzü İstersiniz Efendim?"""))

else:
 print("""Maalesef Şefimiz Bugün O Tür Bir Yemek Yapmadı""")


