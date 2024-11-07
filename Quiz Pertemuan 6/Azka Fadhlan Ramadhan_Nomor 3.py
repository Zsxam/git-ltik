# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

'''Soal:
Bu Rinda merupakan seorang mantan altlet lari dan berencana untuk berlari sore ini.
Running track yang akan digunakan beliau memiliki ukuran panjang 100 meter, lebar
4800 centimeter. Beliau berencana akan berlari sebanyak 10x putaran. Buatlah sebuah
program untuk menghitung total jarak yang akan ditempuh oleh Bu Rinda dalam satuan
kilometer. Gunakan rumus menghitung keliling persegi panjang.'''

panjang_running_track = 100
lebar_running_track = 4800/100 #mengubah ke meter

keliling_track = 2*(panjang_running_track+lebar_running_track)
print("Keliling running track:",keliling_track)

total_jarak = (10*keliling_track)/1000 #mengubah ke km
print(f"Total Jarak yang ditempuh Bu Rinda ketika 10x mengelilingi running track: {total_jarak}km")