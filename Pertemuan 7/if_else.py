umur = int(input("Masukkan Umur: "))

if (umur > 17):
    print("Umur kamu lebih dari 17")
elif (umur >= 18):
    print("Umur kamu lebih dari 18 tahun")
else:
    print("Kamu dibawah umur")

# nested if
if umur > 0:
    if (umur > 17):
        print("Umur kamu lebih dari 17")
    elif (umur >= 18):
        print("Umur kamu lebih dari 18 tahun")
    else:
        print("Kamu dibawah umur")
else:
    print("Kamu bukan manusia")