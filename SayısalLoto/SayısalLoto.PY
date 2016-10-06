"""
@auther: Efecan Altay
@date : 06.10.2016

Name :Sayısal Loto Oyunu

platform : windows10
version : python@3.5.2
"""

import random
import msvcrt
import subprocess as sp

exit = False ;

global para,oynandı,cekilis,kupon

para = 0            

kupon = [0,0,0,0,0,0]   """Kullanıcının oynadığı kuponun datası"""
ad = ""                 """Kullanıcı Adı"""
cekilis = kupon         """Cekiliste Cekilen kuponun datası"""

"""Bilgilerin Gösterildiği fonk."""
def upInfo():
    print("\n##################################")
    print("############_LotoToto_############")
    print("##_"+ad+"_########### Bütçen:" + str(para) +" ##")

"""Ana menü"""
def startMenu():
    upInfo()
    print("A Tuşu : Yeni Oyun")
    print("B Tuşu : Bilgi")
    print("C Tuşu : Çıkış")
    return input("Bir seçenek giriniz: ")

"""Ana menüde A seceği """
def secenekA():
    print("A Tuşu : Kupon Oyna")
    print("B Tuşu : Çıkış")
    return input("Bir seçenek giriniz: ")

"""Ana menüde B seceği """
def secenekB():
    print("\nBu oyun Python Öğrenmeye \n çalışan Efecan Altay tarafından\n yapılmıştır.\n kodlar ve paylaşım açıktır\n Doya Doya Sömürün :D")
    input("\nEnter a bas Menüye Dön...")


    
""" Ana menüde A seçeneğine girildiğinde AA seceneği çalışıyor"""
def secenekAA():
    for i in range(0,6) :
        while(1):
            girilen = input(" kuponun "+str(i+1)+". sayısı:")
            if(aynıSayıDenetle(girilen,kupon) == False):
                kupon[i] = girilen
                break
            else:
                print("Aynı Sayı girmiştiniz,Sayıyı tekrar girin:")
            
    print("\nOynadığın Kupon" + str(kupon))
    while(1):
        onay = input("Onaylıyormusun E/H :")
        if(onay=="E" or onay=="e"):
            break
        elif(onay == "H" or onay =="h"):
            
            break
        else:
            print("Yanlış Girdin") 

"""Çekişin oynandığı fonk"""
def cekilisOyna():
    tutanSayı = 0
    for i in range(0,6):
        cekilis[i] = random.randint(0,49)
    print(cekilis)
    for i in kupon:
        for j in cekilis:
             if(i == j):
                 tutanSayı =tutanSayı+1
    if(tutanSayı > 1):
        print("!!!Kumar Zararlıdır Loto da bir kumardır :D")
        para = 0
        return

"""Secenek yapmayı tekrarlamamak için yazdığım fonk. """
def secim(secenek):
        if (secenek == "A" or secenek == "a"):
            return "A"            
        elif (secenek =="B" or secenek == "b"):
            return "B"
        elif (secenek == "C" or secenek == "c"):
            return "C"
        else:
            print("\n------ErrorMessage-------------\n!!! Böyle Bir giriş yok !!! \nLütfen A , B veya C harflerinden Birini Giriniz.\n-------------------")    
            input("\nDevam için 'Enter' a bas...")
            return -1

"""Ayı sayı girilmemesi için bir denetleme"""
def aynıSayıDenetle(sayi,kupon):
        for i in kupon:
            if(i == sayi):
                return True
        return False
"""
Ana Dögü
"""
while(1):
    
    secilen = secim(startMenu())
    if(secilen == "A"):
        """Kayıt işlemi"""
        para = 10
        a = [2,5,6,4]
        ad = input("adını gir: ")
        print("\n\n##############################")
        print("Hoşgeldin " + ad + "\nKaydın Gerçekleşti")
        print("################################\n\n")
        while(1):
            upInfo()
            secilen = secim(secenekA())
            if(secilen == "A"):
                """Kupon Oyna"""
                secenekAA()
                para -= 2
                print("\n$$$ -2 oynama kesintisi")

                print("##########Çekiliş Sonucu##############")
                cekilisOyna()
                print("######################################")
            elif(secilen == "B"):
                """Menuye Dön Çıkış"""
                break
            else:
                print("!!! A veya B Seceneklerini Girebilirsiniz")
                
    elif(secilen == "B"):
        "Bilgi Ekranı"
        secenekB()
    elif(secilen == "C"):
        "Oyundan çıkış"
        print("Güle Güle :)")
        break
    else:
        print("hata")
