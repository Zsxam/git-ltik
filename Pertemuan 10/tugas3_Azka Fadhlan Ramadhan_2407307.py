# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

def ubahDetik(jam, menit, detik):
    return jam * 3600 + menit * 60 + detik

def perbedaanWaktu(jamMulai, menitMulai, detikMulai, jamAkhir, menitAkhir, detikAkhir):
    totalDetikAwal = ubahDetik(jamMulai, menitMulai, detikMulai)
    totalDetikAkhir = ubahDetik(jamAkhir, menitAkhir, detikAkhir)
    
    perbedaanDetik = totalDetikAkhir - totalDetikAwal
    
    jam = perbedaanDetik // 3600
    perbedaanDetik %= 3600
    menit = perbedaanDetik // 60
    detik = perbedaanDetik % 60
    
    return jam, menit, detik

print("Input Mulai")
jamMulai = int(input("Jam: "))
menitMulai = int(input("Menit: "))
detikMulai = int(input("Detik: "))

print("\nInput Selesai")
jamAkhir = int(input("Jam: "))
menitAkhir = int(input("Menit: "))
detikAkhir = int(input("Detik: "))

perbedaanJam, perbedaanMenit, perbedaanDetik = perbedaanWaktu(
    jamMulai, menitMulai, detikMulai, jamAkhir, menitAkhir, detikAkhir
)

print(f"\nHitung Selisih\nOutput: {perbedaanJam} jam - {perbedaanMenit} menit - {perbedaanDetik} detik")
