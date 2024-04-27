print("Selamat Datang di Aplikasi Perhitungan Mahasiswa")

#Inputan dari nilai mahasiswa
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

#Rumus nilai akhir
nilai_akhir = 0.25 * nilai_tugas + 0.35 * nilai_uts + 0.40 * nilai_uas

#Grade yang akan didapatkan oleh mahasiswa
if nilai_akhir > 85:
    grade = 'A'
elif nilai_akhir > 80:
    grade = 'A-'
elif nilai_akhir > 75:
    grade = 'B+'
elif nilai_akhir > 70:
    grade = 'B'
elif nilai_akhir > 65:
    grade = 'B-'
elif nilai_akhir > 60:
    grade = 'C+'
elif nilai_akhir > 55:
    grade = 'C'
elif nilai_akhir > 50:
    grade = 'C-'
elif nilai_akhir > 30:
    grade = 'D'
else:
    grade = 'E'

#Tampilan akhir yaitu nilai akhir dan grade yang didapatkan mahasiswa
print("Nilai akhir: {:.2f}".format(nilai_akhir))
print("Grade: ", grade)
