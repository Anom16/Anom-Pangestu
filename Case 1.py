print("PROGRAM HITUNG NILAI RATA-RATA\n")

nama = input('Masukan Nama Siswa            : ')
nilai1 = float(input('Masukan Nilai Pertandingan 1 : '))
nilai2 = float(input('Masukan Nilai Pertandingan 2 : '))
nilai3 = float(input('Masukan Nilai Pertandingan 3 : '))

print("\n HASIL NILAI RATA-RATA SISWA")
nilai4 = (nilai1 + nilai2 + nilai3) / 3
juara = "juara ke-1" if nilai4 >= 80 else "juara ke-2" if nilai4 >= 75 else "juara ke-3" if nilai4 >= 65 else "tidak juara"
print(f"\nSiswa yang bernama {nama} memperoleh nilai rata-rata {nilai4} dan menjadi {juara} dari hasil perlombaan yang diikutinya")