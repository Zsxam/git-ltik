# set = himpunan

a = {"apel","apel", "jeruk", "ceri", "durian"}
print(a)

for item in a:
    print(item)

a.add("semangka")
print(a)

b = {"strawberry", "blueberry"}
a.update(b) #Menambah item di set dari set lainnya (bisa juga digunakan untuk menambahkan item dari list dan tuple)
c = a.union(b) #Menambah item di set dari set lainnya di variabel baru
print(a)
print(c)

num = {10,20,20,30,40,50,50,60}
num_2 = {10,20,30,40,50,60}

num.intersection_update(num_2) #menyimpan item yang sama dari dua buah set (irisan)
num_3 = num.intersection(num_2) #menyimpan item yang sama dari dua buah set (irisan) di variabel baru
print(sorted(num))
print(sorted(num_3))

b_2 = {"strawberry", "blueberry", "apel", "jeruk"}
c = a.symmetric_difference(b_2) #Hanya menyimpan item yang berbeda dari dua buah set
a.symmetric_difference_update(b_2) #Hanya menyimpan item yang berbeda dari dua buah set di variabel baru
print(a)
print(c)

a.remove("ceri")
print(a)
a.pop()
print(a)

a.clear()
print(a)