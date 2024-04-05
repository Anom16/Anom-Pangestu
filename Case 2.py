print("PROGRAM HITUNG NILAI AKHIR SISWA\n")

nama = input('Masukan Nama Siswa              : ')
nilai1 = float(input('Masukan Nilai Keaktifan : '))
nilai2 = float(input('Masukan Nilai Tugas     : '))
nilai3 = float(input('Masukan Nilai Ujian     : '))

print("\n HASIL NILAI AKHIR SISWA")
print(f"Siswa yang bernama {nama}")
print('Dengan Nilai Persentasi yang dihasilkan.')
a=nilai1*0.2
b=nilai2*0.5
c=nilai3*0.3
d=a+b+c
grade = "Grade A" if d >= 80 else "Grade B" if d >= 70 else "Grade C" if d >= 56 else "Grade D" if d >= 45 else "Grade E"
print (f'Nilai Keaktifan * 20% : {a}')
print (f'Nilai Tugas * 50% : {b}')
print (f'Nilai Ujian * 30% : {c}')
print(f"Jadi siswa yang bernama {nama} memperoleh nilai akhir sebesar {d} dengan {grade}")
