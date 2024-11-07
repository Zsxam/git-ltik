# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

'''Soal:
Nabila merupakan seorang pemilik online shop. Ia membutuhkan program yang dapat
menyimpan seluruh barang jualan di online shop-nya. Pada bulan Juli lalu,
barang-barang yang dijual oleh online shop Nabila antara lain:

T-Shirt, Blouse, Kemeja, Celana Panjang, Rok, Baju Renang, Tas, Topi, Sepatu, dan Sendal

Mulai bulan ini, online shop tersebut berhenti berjualan Topi dan diganti menjadi
Dompet. Selain itu, karena banyaknya permintaan pelanggan, kini online shop-nya pun
memproduksi Jepitan Rambut dan Kerudung. Program yang Nabila butuhkan harus
dapat menampilkan daftar barang jualan pada bulan Juli berserta jumlah jenis
barangnya dan daftar barang jualan bulan ini berserta jumlah jenis barangnya. Buatlah
program yang dapat memenuhi kebutuhan Nabila.'''

barang_jualan_juli = ["T-Shirt", "Blouse", "Kemeja", "Celana Panjang", "Rok", "Baju Renang", "Tas", "Topi", "Sepatu", "Sendal"]
jumlah_jualan_juli = len(barang_jualan_juli)

print(f"List Jenis Barang yang Dijual Bulan Juli: {barang_jualan_juli}\nJumlah Jenis Barang yang Dijual Bulan Juli: {jumlah_jualan_juli}\n")

barang_jualan_ini = list(barang_jualan_juli) # Mengambil item yang ada di barang_jualan_juli
barang_jualan_ini[7] = "Dompet"
barang_jualan_ini.append("Jepitan Rambut")
barang_jualan_ini.append("Kerudung")
jumlah_jualan_ini = len(barang_jualan_ini)

print(f"List Jenis Barang yang Dijual Bulan ini: {barang_jualan_ini}\nJumlah Jenis Barang yang Dijual Bulan ini: {jumlah_jualan_ini}")
