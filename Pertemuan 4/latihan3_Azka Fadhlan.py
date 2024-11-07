# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

student_info = {
    "Alice": {"age": 20, "Major": "Computer Science"},
    "Bob": {"age": 21, "Major": "Mathematics"},
    "Charlie": {"age": 19, "Major": "Physics"},
}

student = str(input("Masukkan nama siswa: "))
if student in student_info:
    print(f"Umur {student} adalah {student_info[student]['age']} dan Prodinya adalah {student_info[student]['Major']}")
else:
    print("Nama tersebut tidak ada di data")