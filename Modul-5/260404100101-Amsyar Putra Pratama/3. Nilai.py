def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = tugas * 0.30 + uts * 0.30 + uas * 0.40
    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"
    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"
    return nama, nilai_akhir, grade, status

n = int(input("Masukkan jumlah mahasiswa: "))
data_mahasiswa = []

for i in range(n):
    print(f"\nData mahasiswa ke-",i+1)
    nama = input("Nama        : ")
    tugas = float(input("Nilai tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))
    hasil = hitung_nilai(nama, tugas, uts, uas)
    data_mahasiswa.append(hasil)

print("\n=== HASIL NILAI MAHASISWA ===")
for nama, nilai_akhir, grade, status in data_mahasiswa:
    print(f"Nama        : {nama}")
    print(f"Nilai akhir : {nilai_akhir:.2f}")
    print(f"Grade       : {grade}")
    print(f"Status      : {status}")
    print()