# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

list_buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
print(list_buah)

# Nomor 1
list_buah[2] = "cherry"
print("1. ", list_buah)

# Nomor 2
value_user = input("Masukkan value: ")
index_user = int(input("Masukkan index: "))
list_buah.insert(index_user,f"{value_user}")
print("2. ", list_buah)

# Nomor 3
list_buah.sort()
print("3. ", list_buah)