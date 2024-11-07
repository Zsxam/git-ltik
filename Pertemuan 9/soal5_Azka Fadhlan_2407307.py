# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

listbilangan = [0]
bilanganMembesar = []
kurangDari = 0

while kurangDari < 3:
    bilangan = int(input("Input Bilangan : "))
    if bilangan > listbilangan[-1]:
        bilanganMembesar.append(bilangan)
        kurangDari = 0
    else:
        kurangDari += 1
    listbilangan.append(bilangan)

bilanganMembesar.pop(0) # Agar bilangan pertama yang di input dihapus dari list
print(f"\nHasil Penjumlahan Nilai yang Membesar: {sum(bilanganMembesar)}")