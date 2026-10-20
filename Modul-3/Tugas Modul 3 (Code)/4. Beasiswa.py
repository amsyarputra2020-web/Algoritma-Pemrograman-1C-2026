jumlah_penuh = 0

for i in range(1, 11):
    print("Mahasiswa ke:", i)
    nama = input("Nama                   : ")
    ipk = float(input("IPK                    : "))
    penghasilan = int(input("Penghasilan ortu/bulan : "))
    if ipk < 3.00:
        print(nama, ": IPK < 3.00, dilewati")
        continue
    if penghasilan <= 3000000:
        print(nama, ": BEASISWA PENUH\n")
        jumlah_penuh += 1
    elif penghasilan <= 5000000:
        print(nama, ": BEASISWA SEBAGIAN\n")
    else:
        print(nama, ": TIDAK dapat beasiswa\n")
    if jumlah_penuh == 3:
        print("Kuota penuh (3), seleksi dihentikan!")
        break
    print("Total beasiswa penuh:", jumlah_penuh)