import datetime


class Kitap:
    def __init__(self, ad, yazar, yil):
        self.ad = ad
        self.yazar = yazar
        self.yil = yil

    def __str__(self):
        return f"Adı: {self.ad}, Yazarı: {self.yazar}, Yılı: {self.yil}"


class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, ad, yazar, yil):
        guncel_yil = datetime.datetime.now().year

        while True:
            try:
                yil = int(yil)
                if 867 <= yil <= guncel_yil:
                    break
                else:
                    print(f"Yayın yılı geçerli bir yıl olmalıdır.")
            except ValueError:
                print("Lütfen geçerli bir yıl (sayı) girin.")
            yil = input("Yayın yılı: ")

        yeni_kitap = Kitap(ad, yazar, yil)
        self.kitaplar.append(yeni_kitap)
        print(f"'{ad}' kitabı başarıyla eklendi!")

    def kitap_cikar(self, ad):
        for kitap in self.kitaplar:
            if kitap.ad.lower() == ad.lower():
                self.kitaplar.remove(kitap)
                print(f"'{ad}' kitabı başarıyla silindi!")
                return
        print(f"'{ad}' kitabı bulunamadı!")

    def Adina_gore_ara(self, ad):
        sonuc = [kitap for kitap in self.kitaplar if ad.lower() in kitap.ad.lower()]
        if sonuc:
            print(f"'{ad}' kelimesi geçen kitaplar:")
            for kitap in sonuc:
                print(kitap)
        else:
            print(f"'{ad}' adında bir kitap bulunamadı.")

    def Yazara_gore_ara(self, yazar):
        sonuc = [kitap for kitap in self.kitaplar if yazar.lower() in kitap.yazar.lower()]
        if sonuc:
            print(f"'{yazar}' adlı yazarın kitapları:")
            for kitap in sonuc:
                print(kitap)
        else:
            print(f"'{yazar}' adlı yazarın kitabı bulunamadı.")

    def kitaplari_listele(self):
        if self.kitaplar:
            print("Kütüphanedeki kitaplar:")
            for kitap in self.kitaplar:
                print(kitap)
        else:
            print("Kütüphanede hiç kitap yok!")


def main():
    kutuphane = Kutuphane()

    while True:
        print("\nKütüphane Kitap Arama Sistemi")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. İsme Göre Ara")
        print("4. Yazara Göre Ara")
        print("5. Tüm Kitapları Listele")
        print("6. Çıkış")

        secim = input("Seçiminizi yapın: ")

        match secim:
            case "1":
                ad = input("Kitap adı: ")
                yazar = input("Yazar adı: ")
                yil = input("Yayın yılı: ")
                kutuphane.kitap_ekle(ad, yazar, yil)
            case "2":
                ad = input("Silmek istediğiniz kitabın adı: ")
                kutuphane.kitap_cikar(ad)
            case "3":
                ad = input("Aramak istediğiniz kitabın adı: ")
                kutuphane.Adina_gore_ara(ad)
            case "4":
                yazar = input("Aramak istediğiniz yazar adı: ")
                kutuphane.Yazara_gore_ara(yazar)
            case "5":
                kutuphane.kitaplari_listele()
            case "6":
                print("Çıkış yapılıyor. İyi günler!")
                break
            case _:
                print("Geçersiz seçim! Lütfen tekrar deneyin.")

main()