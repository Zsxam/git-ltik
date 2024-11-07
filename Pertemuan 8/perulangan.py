jumlah_perulanan = 2

for index in range(jumlah_perulanan): # For digunakan untuk perulangan yang diketahui jumlah pengulangannya
    print(f"Print ke-{index}")
for i in "Kontol":
    print(f"Huruf: {i}")
for i in range(1,6):
    print(f"Angka: {i}")

buah = ["apel", "belimbing", "ceri", "durian"]

for i in buah: # Perulangan dari suatu list
    print(f"Buah: {i}")
for i in range(1,3): # Perulangan list dengan range()
    print(f"Buah: {buah[i]}")

while(jumlah_perulanan > 1): # while digunakan untuk perulangan yang tidak diketahui jumlah pengulangannya (jika statement memenuhi maka akan dilakukan perulangan)
    print(f"Angka sekarang: {jumlah_perulanan}")
    jumlah_perulanan -= 1 #jika tidak memakai ini, akan terjadi infinite loop (tidak pernah false)

angka = [1,2,3,4,5]

for i in angka:
    if i == 3:
        continue # memberhentikan iterasi loop saat konfisi i = 3
    print(i)

for i in range(10, 0, -1): # Menggunakan range untuk pengulangan naik ke atas, bisa juga untuk menurun
    print(i)

baris = 0
bintang = 0

