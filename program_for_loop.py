# memasukkan jumlah orang
count = int(input("Jumlah orang: "))

# membuat container untuk masukin data yang nanti diinput
nama_pelanggan = []
umur_pelanggan = []

# menginput data satu-satu ke container dengan loop input
for i in range(count):
    print("Data ke {}", format(i+1)) #format itu untuk input datanya, i+1 karena default python mulai dari 0
    nama = input("Nama: ")
    umur = int(input("Umur"))

nama_pelanggan.append(nama) # data nama dimasukkan ke kontainer nama_pelanggan
umur_pelanggan.append(umur) # data umur dimasukkan ke kontainer umur_pelanggan

# print outputnya
for i in range(len(nama_pelanggan)):
    print("Pelanggan {} berusia {}", format(nama_pelanggan[i], umur_pelanggan[i]))
