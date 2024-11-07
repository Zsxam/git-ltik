# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

nilai = float(input("Masukkan Nilai: "))

if(0 <= nilai <= 100):
    if (nilai >= 90):
        tingkat = "A"
        print(f"Nilai {nilai} anda adalah {tingkat}")
    elif (80 <= nilai < 90):
        tingkat = "B"
        print(f"Nilai {nilai} anda adalah {tingkat}")
    elif (70 <= nilai < 80):
        tingkat = "C"
        print(f"Nilai {nilai} anda adalah {tingkat}")
    elif (nilai < 70):
        tingkat = "D"
        print(f"Nilai {nilai} anda adalah {tingkat}")
else:
    print("Masukkan angka antara 0-100")