# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

n = int(input("Masukkan nilai N : "))
urut = 0
bilPrima = []

while n > 0:
    urut += 1
    bilangan = int(input(f"Masukkan bilangan ke-{urut} : "))
    is_prima = True
    for i in range(2, bilangan):
        if bilangan % i == 0:
            is_prima = False
    if is_prima == True:
        bilPrima.append(bilangan)
    n -= 1

if len(bilPrima) != 0:
    print(f"Jumlah bilangan prima adalah {sum(bilPrima)}")
else:
    print("Tidak ada item list yang bilangan prima")


