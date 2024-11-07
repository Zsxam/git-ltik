a = ["apel", "jeruk", "ceri", "durian", "apel"]

# melihat jumlah list
b = len(a)
print(b)

# mengambil nilai
print(a[2])

# slicing
print(a[1:5])

# menambah nilai di akhir list
a.append("sirsak")
print(a)

# update nilai
a[2] = "cherry"
print(a)

# menambah nilai pada index tertentu
a.insert(3, "nangka")
print(a)

# mengapus nilai di index tertentu
a.pop(6)
print(a)

# list bisa berisi tipe data campuran 
c = [1,2,"aku", True, 10.2]
print(c)

# menggabungkan nilai dari list lain
# a.extend(c)
# print(a)

# mengurutkan sesuai abjad (asc) (tipe data tidak boleh berbeda)
a.sort()
print(a)

# mengurutkan dari z ke a (desc) (tipe data tidak boleh berbeda)
# a.reverse()
a.sort(reverse= True)
print(a)

# list method
'''
clear()
copy()
count()
extend()
index()
remove() menghapus berdasarkan nilai. contoh: remove("nangka") n/: menghapus dari index yang paling kecil
reverse()
sort()
'''