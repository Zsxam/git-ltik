# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

nilai = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]
print("List nilai",nilai)

# A. 
# Nilai maksimum
print("Nilai maksimum:", max(nilai))

# Nilai minimum
print("Nilai minimum:", min(nilai))

# rata-rata 
rerata = sum(nilai) / len(nilai)
print("Rata-rata nilai:", rerata)

# B.
# Angka terbesar kedua  
# sort_nilai = sorted(nilai, reverse=True)
nilai.sort(reverse=True)
nilai_terbesar_kedua = nilai[1]
print("Nilai terbesar kedua:", nilai_terbesar_kedua)