# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 18:25:47 2020

@author: Furkan Güven
"""
import time

print('ÇEVRE HESAPLAMA PROGRAMINA HOŞGELDİNİZ....  SİZ SADECE VERİLERİ GİRİN')
print('BİZ SİZİN İÇİN HEZAPLAYALIM.')
print('Lütfen Bekleyiniz')
time.sleep(4)
kullanıcıadı = input("kullanıcı adınız:")
parola = input("Parolanız:")
if not kullanıcıadı == "furkan": 
   print("yanlış kullanıcı adı ")
   time.sleep(1)
if not parola == "123456": 
   print("yanlış parola ")
   time.sleep(5)
     
while(kullanıcıadı == "furkan" and parola == "123456"):
 print('eğer dairenin yada çemberin çevresini hesaplayacaksınız hesaplayıcımız pi değerini 3,14 olarak alır.')
 sekil = int(input("Kare çevre için 1 daire çevre için 2 üçgen çevre için 3 dikdortgen çevre için 4'e basınız."))

 if sekil == 1:
    karekenar = float(input("Karenin bir kenar uzunluğu ne kadar?"))
    print(4 * karekenar)
    time.sleep(15)
 elif sekil == 2:
    dairecevre = float(input("Dairenin yada çemberin çapı ne kadar?"))
    print(3.14 * dairecevre)
    time.sleep(15)
 elif sekil == 3:
    ucgen1 = float(input("Üçgenin ilk kenarının uzunluğu ne kadar?"))
    ucgen2 = float(input("Üçgenin ikinci kenarının uzunluğu ne kadar?"))
    ucgen3 = float(input("Üçgenin üçüncü kenarının uzunluğu ne kadar?"))
    if ucgen1 + ucgen2 <= ucgen3:
        print('böyle üçgen olmaz dostum')
        time.sleep(15)
    elif ucgen2 + ucgen3 <= ucgen1:
        print("böyle üçgen olmaz dostum")
        time.sleep(15)
    elif ucgen3 + ucgen1 <= ucgen2:
        print('böyle üçgen olmaz dostum')
        time.sleep(15)
    else:
        print(ucgen1 + ucgen2 + ucgen3)     
        time.sleep(15)
 elif sekil == 4:
     kısakenar = float(input("Dikdörtgenin kısa kenarının uzunluğu ne kadar?"))
     uzunkenar = float(input("Dikdörtgenin uzun kenarının uzunluğu ne kadar?"))
     if kısakenar > uzunkenar:
         print("kısa kenarın uzun kenarda daha uzun olduğunu ilk defa senden duydum")
         time.sleep(15)
     elif kısakenar == uzunkenar:
         print("Bu kare değil dostum.")
         time.sleep(15)
     else:
         print((kısakenar + uzunkenar) * 2)
         time.sleep(15)
 else:
     print("hatalı giriş yaptınız kare için 1 daire için 2 üçgen için 3 dikdörtgen için 4 e basınız")
     print("program 5 sn sonra kapanacak yine hesaplamak için programı tekrardan açınız.")
     time.sleep(5)
     

    
