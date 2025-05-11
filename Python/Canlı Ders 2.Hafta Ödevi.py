#kullanıcıdan alınan sayının pozitif mi, negatif mi yoksa sıfır mı olduğunu kontrol eden program:
sayi1 = int(input("Bir sayı girin: "))

if sayi1 > 0:
    print("Pozitif sayı")
elif sayi1 < 0:
    print("Negatif sayı")
else:
    print("Sıfır")

#kullanıcıdan alınan sayının tek mi çift mi olduğunu kontrol eden program:
sayi2 = int(input("Bir sayı girin: "))

if sayi2 % 2 == 0:
    print("Çift sayı")
else:
    print("Tek sayı")

#kullanıcının girdiği notu harf notuna çeviren program: (80-100 A, 60-80 B, 40-60 C, 40'tan küçükse F)
not_degeri = int(input("Notunuzu girin: "))

if not_degeri >= 80:
    print("A")
elif not_degeri >= 60:
    print("B")
elif not_degeri >= 40:
    print("C")
else:
    print("F")

#kullanıcın girdiği ismin karakter sayısı uzun mu, değil mi kontrol eden program: 
isim = input("İsminizi girin: ")

if len(isim) > 5:
    print("Uzun isim")
else:
    print(isim)

#kullanıcıdan alınan sayısın asal olup olmadığını kontrol eden program:
sayi3 = int(input("Bir sayı girin: "))

for i in range(2, sayi3):
    if sayi3 % i == 0:
        print("Asal sayı değil")
        break
else:
    print("Asal sayı")

#notlar = [45,85,75,50] içerisinde 75 değerinin indisini yazdıran program:
notlar = [45,85,75,50]

for i in range(len(notlar)):
    if notlar[i] == 75:
        print(i)
        break

#kullanıcıdan alınan sayının faktöriyelini hesaplayan program: 
sayi4 = int(input("Bir sayı girin: "))

faktoriyel = 1

for i in range(1, sayi4 + 1):
    faktoriyel *= i

print(faktoriyel)

#kullanıcıdan pozitif bir sayı alana kadar tekrar tekrar sayı girmesini isteyen program:
sayi5 = -1  

while sayi5 <= 0:
    sayi5 = int(input("Pozitif bir sayı girin: "))
    if sayi5 <= 0:
        print("Lütfen pozitif bir sayı girin!")

#kullanıcıdan alınan sayının asal olup olmadığını fonksiyon kullanarak kontrol eden  program:
sayi6 = int(input("Bir sayı girin: "))
def asal_mi(sayi6):
    for i in range(2, sayi6):
        if sayi6 % i == 0:
            return False
    return True

if asal_mi(sayi6):
    print("Asal sayı")
else:
    print("Asal sayı değil")

#kullanıcıdan alınan sayının faktöriyelini fonksiyon kullanarak hesaplayan program:
sayi7 = int(input("Bir sayı girin: "))

def faktoriyel(sayi7):
    faktoriyel = 1
    for i in range(1, sayi7 + 1):
        faktoriyel *= i
    return faktoriyel

print(faktoriyel(sayi7))