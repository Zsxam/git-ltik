# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

n = 0
o = 0

while n >= 0:
    n = int(input("Masukkan angka: "))
    if n < 0:
        break
    print(f"{o} + {n}")
    o += n
    print(f"= {o}")

print(f"Jumlah dari perulangan diatas adalah: {o}")