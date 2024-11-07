# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

angka = int(input("Masukkan angka: "))

if (angka > 0):
    if (angka % 2) == 0:
        print(f"Bilangan {angka} adalah bilangan Positif dan termasuk bilangan Genap")
    elif (angka % 2) == 1:
        print(f"Bilangan {angka} adalah bilangan Positif dan termasuk bilangan Ganjil")
elif (angka < 0):
    if (angka % 2) == 0:
        print(f"Bilangan {angka} adalah bilangan Negatif dan termasuk bilangan Genap")
    elif (angka % 2) == 1:
        print(f"Bilangan {angka} adalah bilangan Negatif dan termasuk bilangan Ganjil")
else:
    print("Jangan masukin 0 kocak")
