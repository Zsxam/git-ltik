# List
print("Ini bagian tugas list")
list_buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
print(list_buah)

# Nomor 1
print("1. ", list_buah[2:6]) 

# Nomor 2
# del list_buah[4] atau list_buah.pop(4)
list_buah.pop(4)
print("2. ", list_buah)

# Nomor 3
list_buah[2] = "cherry"
print("3. ", list_buah)

# Nomor 4
list_buah.insert(3,"strawberry")
print("4. ", list_buah)

# Nomor 5
list_buah.sort()
print("5. ", list_buah)


# Tuple
print("\nIni bagian tugas tuple")
tuple_buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")
print(tuple_buah)

# Nomor 1
print("1. ", tuple_buah[2:6])

# Nomor 2
print(tuple_buah)
mutasi_tuple_buah = list(tuple_buah)
mutasi_tuple_buah.remove("durian")
tuple_buah = tuple(mutasi_tuple_buah)
print("2. ", tuple_buah)

# Nomor 3
mutasi_tuple_buah = list(tuple_buah)
mutasi_tuple_buah.insert(2,"manggis")
tuple_buah = tuple(mutasi_tuple_buah)
print("3. ", tuple_buah)