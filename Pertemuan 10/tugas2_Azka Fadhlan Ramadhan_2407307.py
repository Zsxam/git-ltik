# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

def login():
    password = "Latihan"
    maxKesempatan = 3

    kesempatan = 0
    print("Login dengan 3 Kesempatan Admin\n")
    while kesempatan != maxKesempatan:
        usn = input("Masukkan username: ")
        pw = input("Masukkan password: ")

        if pw == password:
            print("Login berhasil! Selamat datang.")
            return  
        else:
            kesempatan += 1
            print(f"Password salah. Anda memiliki {maxKesempatan - kesempatan} kesempatan lagi.")

    # If kesempatan are exhausted
    print("Anda telah gagal login sebanyak 3 kali. Silakan coba lagi nanti.")

login()
