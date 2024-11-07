# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

a = ("Ayam", "Sapi", "Kambing", "Kelinci", "Unta")
print(a)

# insert pada tuple
x = list(a)
x.insert(2, "Kucing")
a = tuple(x)
print("1. ", a)

# append pada tuple
y = list(a)
y.append("Anjing")
a = tuple(y)
print("2. ", a)

# pop pada tuple
z = list(a)
z.pop(-1)
a = tuple(z)
print("3. ", a)