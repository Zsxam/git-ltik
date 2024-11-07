# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

bebek = int(input("Masukkan Banyak Bebek : "))

while bebek > 0:
    print(f"\n{bebek} bebek kecil berenang\nMenyusuri sungai yang deras\nInduknya mencari kwek kwek kwek")
    bebek -= 1
    if bebek > 0:
        print(f"Hanya {bebek} ekor yang pulang")
    else:
        print("Dan semua bebek kecil pulang, aha!")