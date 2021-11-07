#fungsi init: ketika membuat class, atribut/karakter yg ada di blueprint hrs ada di bwh fungsi init
#nanti masukin objek ke dalam class/pas nulis objek, blueprint nya dipanggil

class mobil:
    def __init__(ciri, warna, merk, tipe, nomor):
        ciri.warna = warna
        ciri.merk = merk
        ciri.tipe = tipe
        ciri.bahan_bakar = "bensin" #tidak perlu masukkan nilai, jd di atas ga perlu ditambahin
        ciri.roda = 4 #tidak perlu masukkan nilai, jd di atas ga perlu ditambahin
        ciri.nomor = nomor
        
    def myfunc(ciri):
        print("Mobil bahan bakarnya {} dan rodanya {}, tapi warna merk dan tipenya berbeda-beda".format(ciri.bahan_bakar,ciri.roda))
        print("Mobil ke-" + ciri.nomor)
        print("Warna mobil saya " + ciri.warna)
        print("Merk mobil saya " + ciri.merk)
        print("Tipe mobil saya " + ciri.tipe)

m1 = mobil("Merah", "Ford", "Mustang", "1")
m2 = mobil("Biru", "Toyota", "Prius", "2")
m3 = mobil("Hijau", "Volkswagen", "Golf", "3")

m1.myfunc()
m2.myfunc()
m3.myfunc()