# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

kesempatan = 3

print("Silahkan Login\n")
while kesempatan > 0:
    usn = input("Username : ")
    pw = input("Password : ")

    if(usn == "loginUTS") and (pw == "rpl2024"):
        print("\nSelamat Datang di Aplikasi Prodi RPL!")
        kesempatan = 0
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(f"\nLogin Salah! Kesempatan Anda {kesempatan}x lagi.\n")
        else:
            print("\nAnda Tidak Diperkenankan Mengakses Aplikasi Ini.")