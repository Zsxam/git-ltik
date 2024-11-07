kucing = {
    "nama": "Kuro",
    "umur": 2,
    "ras": "Persian",
    "jantan": True,
    "hobi": ["makan", "tidur"]
}
print(kucing)
print(len(kucing))
print(kucing["nama"])
print(kucing.get("ras"))
print(kucing.keys())
print(kucing.values())

kucing["umur"] = 1.5 # Mengubah value
print(kucing)

kucing["lucu"] = True # Menambah key & value
print(kucing)

kucing.update({"umur": 2 , "ras": "kampung"})
print(kucing)

kucing.update({"warna": ["putih", "hitam"]})
print(kucing)

kucing.pop("jantan") # Menghapus item berdasarkan key, Tidak boleh kosong argumennya
print(kucing)

# memanggil dictionary dalam dictionary (nested dictionary)
student_info = {
    "Alice": {"age": 20, "Major": "Computer Science"},
    "Bob": {"age": 21, "Major": "Mathematics"},
    "Charlie": {"age": 19, "Major": "Physics"},
}

student = str(input("Masukkan nama siswa: "))
print(f"Umur {student} adalah {student_info[student]['age']} dan Prodinya adalah {student_info[student]['Major']}")