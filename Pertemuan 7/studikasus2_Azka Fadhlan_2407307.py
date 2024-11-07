# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

print("-----------Aplikasi Prdiksi Model Catwalk-----------")

gender = str(input("Masukkan gender kamu (P/L): "))

if(gender.lower() == "l"):
    umur = int(input("Masukkan umur: "))
    if(18 <= umur <= 25):
        print("-----Umur kamu memenuhi kriteria kami-----")
        tinggi = int(input("Masukkan tinggi badan: "))
        if(tinggi >= 175):
            print("-----Tinggi kamu memenuhi kriteria kami-----")
            iq = float(input("Masukkan IQ kamu: "))
            if(iq >= 130):
                print("-----IQ kamu memenuhi kriteria kami-----")
                print(f"SELAMATT!! Kamu Cocok jadi Model Catwalk Pria!")
                data = {
                    "Gender": gender,
                    "Umur": umur,
                    "Tinggi": tinggi,
                    "IQ": iq,
                }
                print("Ringkasan data kamu: \n",data)
            else:
                print(f"-----Maaf, kamu tidak cocok menjadi model catwalk karena iq kamu kurang dari 130-----")
        else:
            print(f"-----Maaf, kamu tidak cocok menjadi model catwalk karena tinggi kamu kurang dari 175cm-----")
    else:
        print(f"-----Maaf, kamu tidak cocok menjadi model catwalk karena umur kamu tidak masuk kriteria kami (18-25 tahun)-----")
elif(gender.lower() == "p"):
    umur = int(input("Masukkan umur: "))
    if(18 <= umur <= 25):
        print("-----Umur kamu memenuhi kriteria kami-----")
        tinggi = int(input("Masukkan tinggi badan: "))
        if(tinggi >= 170):
            print("-----Tinggi kamu memenuhi kriteria kami-----")
            iq = float(input("Masukkan IQ kamu: "))
            if(iq >= 130):
                print("-----IQ kamu memenuhi kriteria kami-----")
                print(f"SELAMATT!! Kamu Cocok jadi Model Catwalk Wanita!!")
                data = {
                    "Gender": gender,
                    "Umur": umur,
                    "Tinggi": tinggi,
                    "IQ": iq,
                }
                print("Ringkasan data kamu: \n",data)
            else:
                print(f"-----Maaf, kamu tidak cocok menjadi model catwalk karena iq kamu kurang dari 130-----")
        else:
            print(f"-----Maaf, kamu tidak cocok menjadi model catwalk karena tinggi kamu kurang dari 170cm-----")
    else:
        print(f"-----Maaf, kamu tidak cocok menjadi model catwalk karena umur kamu tidak masuk kriteria kami (18-25 tahun)-----")
else:
    print(f"Kamu LGBT, silahkan tobat dahulu")

