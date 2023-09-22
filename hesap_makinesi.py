def hesapla():
    islem = input("Birer boşluk bırakarak 2 sayı ve bir işlem sembolü giriniz (Örnek: 1 3 *): ").split()

    try:
        sayi_1 = float(islem[0])
        sayi_2 = float(islem[1])
        sembol = islem[2]

        if sembol == "+":
            sonuc = sayi_1 + sayi_2
            print(sonuc)
        elif sembol == "-":
            sonuc = sayi_1 - sayi_2
            print(sonuc)
        elif sembol == "/":
            sonuc = sayi_1 / sayi_2
            print(sonuc)
        elif sembol == "*":
            sonuc = sayi_1 * sayi_2
            print(sonuc)
        else:
            print("Lütfen yazdığınız sembollerin geçerli olduğundan emin olunuz. (+, -, /, *)")
            hesapla()

    except ValueError:
        print("lütfen geçerli bir sayı giriniz.")
        hesapla()
    except IndexError:
        print("Lütfen doğru formatta giriş yaptığınızdan emin olun. sayı sayı sembol")
        hesapla()


hesapla()
