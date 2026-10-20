n = int(input("Masukkan tinggi setengah menara (2–15): "))
while n < 2 or n > 15:
    print("Nilai harus antara 2 dan 15.")
    n = int(input("Masukkan tinggi setengah menara (2–15): "))
for baris in range(1, n + 1):
    spasi = " " * (n - baris)
    naik  = ""
    for angka in range(1, baris + 1):
        naik += str(angka % 10)
    turun = ""
    for angka in range(baris - 1, 0, -1):
        turun += str(angka % 10)
    print(spasi + naik + turun)
for baris in range(n - 1, 0, -1):
    spasi = " " * (n - baris)
    naik  = ""
    for angka in range(1, baris + 1):
        naik += str(angka % 10)
    turun = ""
    for angka in range(baris - 1, 0, -1):
        turun += str(angka % 10)
    print(spasi + naik + turun)