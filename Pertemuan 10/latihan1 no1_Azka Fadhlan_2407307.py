# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

def fibonacci(n):
    a = 0 
    b = 1
    result = []
    
    for _ in range(n): # _ disini digunakan sebagai penanda bahwa variabel tersebut tidak akan dipakai.
        result.append(a)
        a, b = b, a + b  # Perbarui nilai a dan b untuk bilangan berikutnya
        
    return result

jumlah_n = int(input("Masukkan jumlah n dalam deret Fibonacci: "))

deretFibonacci = fibonacci(jumlah_n)
print(f"Deret Fibonacci: {deretFibonacci}")
