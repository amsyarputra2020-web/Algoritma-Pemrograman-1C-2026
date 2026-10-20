data = []
jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0
total_nilai = 0

for i in range(1, 4):
    print("\nMahasiswa ke-", i)
    nama = input("Nama        : ")
    tugas = float(input("Nilai tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))
    nilai_akhir = tugas * 0.30 + uts * 0.30 + uas * 0.40
    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1
    data.append((nama, tugas, uts, uas, nilai_akhir, kategori))
    total_nilai += nilai_akhir
    print("Nilai akhir :", round(nilai_akhir, 2))
    print("Kategori    :", kategori)
print("\n=== HASIL SELURUH MAHASISWA ===")
for m in data:
    print("Nama:", m[0])
    print("Tugas:", m[1], "| UTS:", m[2], "| UAS:", m[3])
    print("Nilai akhir:", round(m[4], 2))
    print("Kategori:", m[5])
    print()
tertinggi = max(data, key=lambda m: m[4])
terendah = min(data, key=lambda m: m[4])
print("Jumlah kategori A:", jumlah_A)
print("Jumlah kategori B:", jumlah_B)
print("Jumlah kategori C:", jumlah_C)
print("Jumlah kategori D:", jumlah_D)
print("Jumlah kategori E:", jumlah_E)

print("Nilai tertinggi:", tertinggi[0],
      round(tertinggi[4], 2))
print("Nilai terendah:", terendah[0],
      round(terendah[4], 2))
print("Rata-rata kelas:", round(total_nilai / 10, 2))