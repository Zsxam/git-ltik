# Contoh Fungsi
def penjumlahan(a,b): # def = fungsi, a dan b adalah parameter (parameter yang ada di fungsi harus terisi semua)
    hasil = a+b
    return hasil

print(penjumlahan(2,5))

# Contoh Prosedur
def greeting(nama):
    print(f"halo, {nama}")

greeting("Aku")

# Default parameter
def hewan(mamalia = "kucing"):
    print("Halo aku", mamalia)

hewan()

# Arbitary Argument = If you do not know how many arguments that will be passed into your function
def funcArgs(*angka):
    print("angka terakhir yang dimasukkan yaitu", angka[-1])

funcArgs(2,4,6,8,10)

# Arbitary Keywords = If you do not know how many keyword that will be passed into your function
def my_function(**kid):
  print("His last name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")

