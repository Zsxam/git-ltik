# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

'''Soal:
Pak Oki memiliki sebuah mobil dengan spesifikasi seperti berikut:
● Merk: Honda
● Tipe: HRV
● Tahun: 2018
● Warna: Hitam
● No. Polisi: D 1234 ABC
● Bensin: Pertalite
● Tranmisi: Manual

Karena usahanya semakin sukses, Pak Oki mengganti mobilnya dengan mobil keluaran
terbaru, yaitu Honda Civic Turbo tahun 2023 bewarna Merah. Mobil baru Pak Oki
menggunakan bensin Pertamax dan transmisinya Automatic. Plat nomor mobil baru
Pak Oki adalah D 0 KI. Buatlah program yang dapat menyimpan detail informasi dari
mobil lama Pak Oki sekaligus dapat mengupdate informasi mobil baru yang dibeli oleh
Pak Oki (berdasarkan inputan). Output program yang diinginkan oleh Pak Oki adalah
sebagai berikut:'''

mobil_pak_oki = {"Merk": "Honda",
                "Tipe": "HRV",
                "Tahun": 2018,
                "Warna": "Hitam",
                "No. Polisi": "D 1234 ABC",
                "Bensin": "Pertalite",
                "Tranmisi": "Manual"}

print(f"Mobil Lama Pak Oki adalah:\nMerk: {mobil_pak_oki["Merk"]}\nTipe: {mobil_pak_oki["Tipe"]}\nWarna: {mobil_pak_oki["Warna"]}\nTahun: {mobil_pak_oki["Tahun"]}\n")

print("Masukkan Informasi Detail Mobil Baru")
merk = input("Merk: ")
tipe = input("Tipe mobil: ")
tahun = input("Tahun keluaran: ")
warna = input("Warna: ")
nopol = str(input("No. Polisi: "))
bensin = input("Bensin: ")
transmisi = input("Transmisi: ")

mobil_pak_oki["Merk"] = merk
mobil_pak_oki["Tipe"] = tipe
mobil_pak_oki["Tahun"] = tahun
mobil_pak_oki["Warna"] = warna
mobil_pak_oki["No. Polisi"] = nopol
mobil_pak_oki["Bensin"] = bensin
mobil_pak_oki["Transmisi"] = transmisi

print(f"\n----------*----------\nMobil Baru Pak Oki adalah:\nMerk: {mobil_pak_oki["Merk"]}\nTipe: {mobil_pak_oki["Tipe"]}\nWarna: {mobil_pak_oki["Warna"]}\nTahun: {mobil_pak_oki["Tahun"]}\n----------*----------")