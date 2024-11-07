# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

nim = int(input("Input 3 digit NIM terakhir : "))

if 0 < nim <= 50:
    if nim % 2 == 1:
        kelas = "K1" 
        print(f"Silahkan masuk ke kelas {kelas}")
    else:
        kelas = "K2"
        print(f"Silahkan masuk ke kelas {kelas}")
elif 50 < nim <= 100:
    if nim % 2 == 1:
        kelas = "K3" 
        print(f"Silahkan masuk ke kelas {kelas}")
    else:
        kelas = "K4"
        print(f"Silahkan masuk ke kelas {kelas}")
elif 100 < nim <= 150:
    if nim % 2 == 1:
        kelas = "K5" 
        print(f"Silahkan masuk ke kelas {kelas}")
    else:
        kelas = "K6"
        print(f"Silahkan masuk ke kelas {kelas}")
elif nim > 150:
    if nim % 2 == 1:
        kelas = "K7" 
        print(f"Silahkan masuk ke kelas {kelas}")
    else:
        kelas = "K8"
        print(f"Silahkan masuk ke kelas {kelas}")
else:
    print("Mohon masukkan 3 digit NIM terakhir dengan benar")


