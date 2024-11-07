# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

bilangan = 0
genap = []
ganjil = []
while bilangan >= 0:
    bilangan = int(input("Input Bilangan : "))

    if bilangan >= 0:
        if (bilangan % 2) == 1:
            ganjil.append(bilangan)
        else:
            genap.append(bilangan) 
    else:
        break

print(f"Jumlah bilangan genap :  {sum(genap)}")
print(f"Jumlah bilangan ganjil : {sum(ganjil)}")
