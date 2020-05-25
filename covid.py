import random
import time
z=("*"*20)
z=z.center(62)
print(z)
print('-'*56)  # Zamandan tasarruf sağlamak ve estetik durmasını sağlamak için bu basit kod satırı kullanıyoruz.
a="\t\tHERKESE MERHABA"
a=a.center(49)
print(a)
time.sleep(1) #ekrana 1 saniye sonra çıktı vermesini istediğimiz için sleep fonksiyonunu kullanıyoruz.
print('-'*56)



import datetime 
now = datetime.datetime.now()
print(now.strftime("        \t\tTARİH:%d-%B-%y SAAT:%H:%M:%S"))  #kullanıcının anketi hangi tarih ve saatte uyguladığını gösteren fonksiyonu kullanıyoruz.
time.sleep(1)
print('-'*56)
k="\t\tKORONA TESTİ"
k=k.center(49) 
print(k)
print('-'*56)




def cor_test():
    print('                        COVID-19 \n ')

    num = int(input(" Kendini nasıl koruman gerektigini görmek için '1'  \n-----------------------------------------------\n COVID 19 semptomlarını görmek için '2'  \n-----------------------------------------------\n Kendini CORONA testine sokmak için '3' : ")) #Kullanıcıdan sayı alıp isteği üzerine devam etmesini input değeri alarak sayı belirtilen sayılardan birisini yazmasını istiyoruz. 
    if num == 1: 
        print("\n           NASIL KORUNURUZ!\n - Ellerinizi sık sık yıkayın. \n - Olabildiğince evde kalın. \n - Dışarı çıkarsanız ya da birileri evine gelirse mesafe kurmayı unutmayın.") # alt alta sıralanmasını istediğimiz için "\n" kullanıyoruz. 
    elif num == 2:
        print("\nBu belirtiler 2-14 gün arasında ortaya çıkabilir.: \n - ATEŞ \n - ÖKSÜRÜK \n - NEFES DARLIĞI") 
    elif num == 3:
        print("-"*58)

        check = int(input(" Eğer ateşiniz var ise '1' yok ise '2'ye basınız: "))
        print("-"*56)
        if check == 1:
            sub = int(input("Eğer nefes alma sorununz var ise '1' yok ise 2'ye basınız: "))
            print("------------------------------------------------------")
            if sub == 1:
                akshat = int(input("Eğer kuru öksürüğünüz var ise '1' yok ise '2'ye basınız: "))
                print("-------------------------------------------------")
                if akshat == 1:
                    print("Corona virüsüne sahipsiniz. ")
                    print("-"*54)
                else:
                    print("Sizde korona virüs semptomları var.")
                    print("-"*46)
            else:
                mummy = int(input("Eğer herhangi bir grip semtomlarınız varsa '1' yok ise '2'ye basınız "))
                if mummy == 1:
                    print("-"*53)
                    print("Sizde korona virüs semptomları var.")
                    print("-"*46)
                else:
                    print("Sizde korona virüs semptomları var.")
                    print("-"*46)
        else:
            tanay = int(
                input("Eğer nefes alma sorununz var ise '1' yok ise '2'ye basınız: "))
            print("-"*53)
            if tanay == 1:
                covid_1 = int(input("Eğer herhangi bir grip semtomlarınız varsa '1' yok ise '2'ye basınız: "))
                print("-"*46)
                if covid_1 == 1:
                    print("Sizde korona virüs semptomları var.")
                    print("-"*46)
                else:
                    print("Sizde korona virüs semptomları var.")
                    print("-"*46)
            else:
                covid_2 = int(input("Eğer herhangi bir grip semtomlarınız varsa 1 yok ise 2'ye basınız: "))
                print("-"*53)
                if covid_2 == 1:
                    print("Sizde korona virüs semptomları var.")
                    print("-"*46)
                else:
                    print("Hiç semptomunuz yok.")
            print("-"*62)

    else:
        print("1,2 veya 3'e bastığından emin ol!")


cor_test()

print("-"*60)
print("\tEğer sizde korona virüs semptomları var ise")
print("\ten yakın hastane ile iletişime geçin ")
print("\n\tLütfen geç olmadan 112 veya 911'i arayın.")

semptomlar = int(input("\n\tEğer hiç semptomunuz yok ise 1'e\n "))
if semptomlar == 1:

    print("\n Karantina için oyunlar:")
    print("-"*62)
    oyun = int(input("\tSayı tahmin etme oyunu için '1'  \n ---------------------------------------------\n\tHangi hayvana benzediginizi görmek için '2'ye basınız\n  "))
    if oyun == 2:
        karakter = [
            'Yarasa', 'Maymun', 'İnek', 'Kaplan', 'Eşşek', 'Bufalo', 'domuz',
            'Fil','Tavşan','Aslan','Orangutan','Karga'
        ]  # içerisinden random bir hayvan çekmesini sağlamak için liste açıyoruz.
        make = random.choice(karakter)  #import olarak random tanımladıktan sonra bilgisayardan listemizde bulunan hayvanlardan rastgele bir tanesini seçmesini istiyoruz.
        print(make)

    elif oyun == 1:

        kazanan_sayı = random.randint(1, 100) # 1 ile 100 arasında rastgele bir sayı üretmesini istiyoruz.
        tahmin = 1
        number = int(input("1 ile 100 arasında sayı tahmin ediniz : ")) # Kullanıcıdan oyun için sayı alındı
        oyun_bitti = False 

        while not oyun_bitti:

            if number == kazanan_sayı:

                print("Bildiniz! ve sayıyı {}.kerede bildiniz".format(tahmin)) # kullanıcı sayıyı bulma aşamasında kaç kere denediğini çıktımızda görebilmemiz için .format kullandık ve {} arasında sayımızı alabiliyoruz.
                oyun_bitti = True
            else:

                if number < kazanan_sayı:

                    print("Çok az! ")

                else:

                    print("Çok fazla! ")

                tahmin = tahmin + 1 # kaç kere tahmin ettiyse çıktısını almak için bir arttırıyoruz.
                number = int(input("Tekrar tahmin et:"))

else:
    print("Teşekkürler.............")

print("\n\t\t\tCREATED BY Yunus")














