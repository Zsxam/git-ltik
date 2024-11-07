# Nama: Azka Fadhlan Ramadhan
# NIM: 2407307
# Kelas: RPL 1B

numbers = [10,20,20,30,40,50,50,60]

# hasil = []
# for index in numbers:
#     if index not in hasil:
#         hasil.append(index) 
# print(hasil)

numbers_list = list(set(numbers))
numbers_list.sort()
print(numbers_list)
