n="1875"
sayi=int(n)
sayi = ((sayi % 9) * k) % 9
sonuc = sayi % 9
if sonuc == 0:
    print(9)
else:
    print(sonuc)
