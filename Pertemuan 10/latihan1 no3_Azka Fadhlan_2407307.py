# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

def nilaiTotalRerata(*bilangan):
    # Menghitung total dan rata-rata
    total = sum(bilangan)
    rerata = total / len(bilangan)
    
    return total, rerata

bilangan = []
    
print("Masukkan nilai satu per satu (ketik 'end' untuk menghentikan)")

while True:
    inputBilangan = input("Masukkan nilai: ")
    
    if inputBilangan.lower() == 'end':
        break
    else:
        bilangan.append(int(inputBilangan))
    
total, rerata = nilaiTotalRerata(*bilangan)
print(f"Total: {total}, Rata-rata: {rerata}")
