# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

def volumeTabung(jari, t):
    pi = 3.14
    la = (jari ** 2) * pi
    print(f"\nLuas alas: {la}")
    hasil = la * t
    return hasil

jari = float(input("Masukkan Jari-jari: "))
t = float(input("Masukkan Tinggi: "))
print(f"Volume Tabungnya adalah: {volumeTabung(jari, t)}")
