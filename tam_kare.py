sayilar = input("Aralarında boşluk bırakarak 2 sayı giriniz. ").split()
print(sayilar)

sayilar[0] = int(sayilar[0])
sayilar[1] = int(sayilar[1])

sonuc = []
for i in range(sayilar[0], sayilar[1] + 1):
    if i**.5 == int(i**.5):
        sonuc.append(i)

print(sonuc)
