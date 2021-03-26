#membuat judul program
print("================================")
print("=== Hasil div suatu bilangan ===")
print("================================")
#mengimpor library math
import math

#memasukkan input 2 angka
angka_1 = int(input("Masukkan angka pertama "))
angka_2 = int(input("Masukkan angka kedua "))

#proses div
hasil = math.floor(angka_1 / angka_2)

#output
print("hasil div dari", angka_1, "dan", angka_2, "adalah", hasil)