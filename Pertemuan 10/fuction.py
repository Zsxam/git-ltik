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

# Arbitary Argument
def funcArgs(*angka):
    print("angka terakhir yang dimasukkan yaitu", angka[-1])

funcArgs(2,4,6,8,10)

# Arbitary Keywords
# nanti

