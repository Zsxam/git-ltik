# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

print("Menggunakan For")
for i in range(1, 51): #pakai for
    if i % 5 == 0:
        print("pass")
    else:
        print(i)

print("\nMenggunakan While")
deret = 0
while deret < 50: #pakai while
    deret += 1
    if (deret%5) == 0:
        print("pass")
        continue
    print(deret)