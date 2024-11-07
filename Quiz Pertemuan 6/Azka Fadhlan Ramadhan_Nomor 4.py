# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

'''Soal: 
Pak Rendi meneliti seberapa lama sebuah mobil balap dapat menyelesaikan 1 putaran.
Mobil balap itu, ternyata mampu melaju cepat sehingga dapat menyelesaikan 1 putaran
hanya dalam waktu 11 menit 30 detik. Buatlah sebuah program untuk membantu Pak
Rendi agar waktu yang didapat tersebut dapat dikonversi satuannya menjadi detik saat
ditampilkan.'''

menit = 11
detik = 30

ubah_ke_detik = menit*60
total_waktu = ubah_ke_detik+detik

print(f"Waktu yang ditempuh mobil balap dalam 1 putaran adalah {menit} menit {detik} detik atau total {total_waktu} detik")