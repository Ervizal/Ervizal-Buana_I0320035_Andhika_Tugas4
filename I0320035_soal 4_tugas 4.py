#membuat judul program
print("===========================================")
print("======== Program rencana pengujian ========")
print("===========================================")

#menyimpan jawaban pertanyaan dalam bentuk variabel
usia = int(input("Masukkan usia anda "))
status = str(input("Apakah Anda sudah lulus ujian kualifikasi (Y/T)? "))

#if else statement
if(usia >= 21 and (status == "Y" or status == "y")):
	print("Anda dapat mendaftar di kursus")
else:
	print("Anda tidak dapat mendaftar di kursus")