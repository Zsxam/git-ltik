# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

'''Soal:
Ibu Novia merupakan salah satu guru Matematika di SMA Bandung, beliau ingin
memiliki program yang dapat menyimpan 10 nilai Matematika siswanya. Adapun
susunan nilainya adalah sebagai berikut:

87.7, 56.5, 93.2, 67.8, 65.0, 38.5, 42.8, 74.5, 89.0, dan 93.2.

Beliau ingin program yang apabila beliau mengetikan no urut siswa, maka program
akan memunculkan nilai dari siswa yang memiliki no. urut tersebut. Sebagai contoh,
ketika beliau mengetikan no. urut 1 maka nilai yang keluar adalah 87.7 dan ketika
mengetikan no. urut 3 maka nilai yang keluar adalah 93.2, dst. Buatlah program yang
dapat memenuhi kebutuhan Bu Novia. (bobot: 20 point)'''

nilai_mtk = [87.7, 56.5, 93.2, 67.8, 65.0, 38.5, 42.8, 74.5, 89.0, 93.2]

no_urut = int(input("Masukkan angka 1-10\nNo Urut: "))

if no_urut >= 1 and no_urut <= 10: # Mencegah user memasukkan angka kurang dari 1 dan angka lebih dari 10
    if no_urut == 1:
        print(f"Nilai Siswa No. Urut 1: {nilai_mtk[0]}")
    if no_urut == 2:
        print(f"Nilai Siswa No. Urut 2: {nilai_mtk[1]}")
    if no_urut == 3:
        print(f"Nilai Siswa No. Urut 3: {nilai_mtk[2]}")
    if no_urut == 4:
        print(f"Nilai Siswa No. Urut 4: {nilai_mtk[3]}")
    if no_urut == 5:
        print(f"Nilai Siswa No. Urut 5: {nilai_mtk[4]}")
    if no_urut == 6:
        print(f"Nilai Siswa No. Urut 6: {nilai_mtk[5]}")
    if no_urut == 7:
        print(f"Nilai Siswa No. Urut 7: {nilai_mtk[6]}")
    if no_urut == 8:
        print(f"Nilai Siswa No. Urut 8: {nilai_mtk[7]}")
    if no_urut == 9:
        print(f"Nilai Siswa No. Urut 9: {nilai_mtk[8]}")
    if no_urut == 10:
        print(f"Nilai Siswa No. Urut 10: {nilai_mtk[9]}")
else:
    print("Tolong masukkan angka antara 1-10")