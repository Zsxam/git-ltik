# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

jumlah_barang = int(input("Masukkan jumlah barang: "))
harga_per_barang = 0

if (jumlah_barang >= 0):
    if (jumlah_barang < 100):
        harga_per_barang = 5000
    elif (jumlah_barang >= 100 and jumlah_barang <= 150):
        harga_per_barang = 4000
    elif (jumlah_barang > 150):
        harga_per_barang = 2500
    print(f"Harga satuan dari {jumlah_barang} barang adalah Rp.{harga_per_barang}")
    print(f"Total harga untuk {jumlah_barang} barang adalah Rp.{harga_per_barang*jumlah_barang}") 
else:
    print("Tolong jangan masukkan angka minus")
