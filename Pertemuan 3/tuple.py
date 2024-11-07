a = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")
print(a)

# untuk index dan menghitung jumlah item sama seperti list

# untuk mengubah item pada tuple, kita harus mengkonversi tuple dlu ke list (untuk menambah dan menghapus juga pakai konversi ini)
x = list(a)
x[2] = ("cherry")
a = tuple(x)
print(a)

# untuk menambah item pada tuple, kita harus mengkonversi tuple dlu ke list (untuk menambah dan menghapus juga pakai konversi ini)
x = list(a)
x.insert(2, "melon")
a = tuple(x)
print(a)

# untuk menambah item di akhir pada tuple, kita harus mengkonversi tuple dlu ke list (untuk menambah dan menghapus juga pakai konversi ini)
x = list(a)
x.append("sukun")
a = tuple(x)
print(a)

# untuk mengubah item pada tuple, kita harus mengkonversi tuple dlu ke list (untuk menambah dan menghapus juga pakai konversi ini)
x = list(a)
x.pop(-1)
a = tuple(x)
print(a)