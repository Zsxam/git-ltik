# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

'''Soal:
Pak Abi berencana untuk membangun rumah baru di kampung halamannya. Beliau
sudah membuat desain rumah yang berbentuk sebagai berikut:

Buatlah sebuah program untuk dapat menghitung total biaya yang Pak Abi harus
keluarkan untuk membuat bangunan tersebut dimana biaya untuk pembuatan
dindingnya yaitu Rp. 450.000/m2. Untuk menghitung luas permukaan dinding gunakan
rumus 2 x (Panjang x Tinggi) + 2 x (Lebar x Tinggi)'''

panjang = 8
lebar = 1000/100 #mengubah ke meter
tinggi = 400/100 #mengubah ke meter

lp_dinding = 2 * (panjang * tinggi) + 2 * (lebar * tinggi)

harga = int(450000*lp_dinding)

print("Panjang:", panjang, "Lebar:", lebar,"Tinggi:", tinggi)
print(f"Luas Permukaan Seluruh Dinding: {lp_dinding}m2")
print(f"Harga yang harus dibayar oleh Pak Abi: Rp.{harga}")


