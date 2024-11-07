# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

students = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics",
} 

hitung_prodi = {}
# for student, prodi in students.items():
#     if prodi in hitung_prodi:
#         hitung_prodi[prodi] += 1
#     else:
#         hitung_prodi[prodi] = 1

# for prodi, jumlah in hitung_prodi.items():
#     print(f"prodi {prodi} sebanyak {jumlah} orang")

hitung_prodi["Computer Science"] = list(students.values()).count("Computer Science")
hitung_prodi["Mathematics"] = list(students.values()).count("Mathematics")
hitung_prodi["Physics"] = list(students.values()).count("Physics")

print(f"prodi computer science sebanyak {hitung_prodi['Computer Science']}")
print(f"prodi mathematics sebanyak {hitung_prodi['Mathematics']}")
print(f"prodi physics sebanyak {hitung_prodi['Physics']}")