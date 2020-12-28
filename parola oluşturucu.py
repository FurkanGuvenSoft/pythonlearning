import time
import string
from random import *
harfler = string.ascii_letters
sayilar = string.digits
semboller = string.punctuation
karakterler = harfler+sayilar+semboller
print("Parola oluşturma programına Hoşgeldiniz!")
time.sleep(1)
yanıt = "h"
while 1<10:
    if yanıt == "h":
        x = int(input("Oluşturmak istediğiniz Parolanın uzunluğu en az kaç karakter olsun?")) 
        y = int(input("Oluşturmak istediğiniz Parolanın uzunluğu en fazla kaç karakter olsun?"))
        min_uzunluk = x
        max_uzunluk = y
        sifre = "".join(choice(karakterler)
        for x in range(randint(min_uzunluk, max_uzunluk)))
        print(sifre)
        yanıt = input('''Parolayı beğendiniz mi? evet için "e" ye hayır için "h" ye basınız''')
    elif yanıt == "e":
        print("Bizi Tercih Ettiğiniz İçin Teşekkürler.")
        break
    else:
        print("Hatalı yada eksik tuşladınız")
        yanıt = "h"
