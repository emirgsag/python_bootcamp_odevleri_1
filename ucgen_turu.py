kenarlar = input("Üçgenin kenarlarını birer boşluk bırakarak giriniz. (Örnek: 10 10 15): ").split()

ucgen_turleri = ["Çeşitkenar", "İkizkenar", "Eşkenar"]

esit_kenar_sayisi = 0

if kenarlar[0] == kenarlar[1]:
    esit_kenar_sayisi += 1

if kenarlar[0] == kenarlar[2]:
    esit_kenar_sayisi += 1

if esit_kenar_sayisi < 1:
    # Sadece yukarıdakilerin ikisi de yanlışsa buraya bakılır.
    if kenarlar[1] == kenarlar[2]:
        esit_kenar_sayisi += 1

ucgen_turu = ucgen_turleri[esit_kenar_sayisi]
print(f"{kenarlar} üçgeni bir {ucgen_turu} üçgenidir.")
