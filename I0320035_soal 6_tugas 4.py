#membuat judul program
print("===========================================")
print("========= Program operasi bitwise =========")
print("===========================================")

a = 4									#4 = 0100
b = 11									#11 = 1011
c = 0

#output dari 4 | 11
c = a | b
print("Hasil dari 4 | 11 adalah", c)	#menghasilkan 15 = 1111

#output dari 4 >> 11
c = a >> b
print("Hasil dari 4 >> 11 adalah", c)	#menghasilkan 0 = 0000 

#output dari 4 ^ 11
c = a ^ b
print("Hasil dari 4 ^ 11 adalah", c)	#menghasilkan 15 = 1111

#output dari ~4
c = ~a
print("Hasil dari ~4 adalah", c)		#menghasilkan -5 = 1011

#output dari 11&4
c = b & a
print("Hasil dari 11 & 4 adalah", c)	#menghasilkan 0 = 0000