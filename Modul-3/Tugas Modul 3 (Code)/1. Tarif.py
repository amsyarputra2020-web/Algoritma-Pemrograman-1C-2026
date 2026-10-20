jumlah_penumpang = 0
total_pendapatan = 0
jarak_terjauh = 0
total_jarak = 0
while True :
    try :
        jarak = int(input("Masukkan jarak tempuh (km), atau 0 untuk selesai: "))
    except ValueError:
        print("Input harus berupa angka bulat.")
        continue
    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak boleh negatif. Silakan masukkan ulang.")
        continue
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500
    jumlah_penumpang += 1
    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        total_pendapatan += tarif
        total_jarak += jarak
        jarak_terjauh = max(jarak_terjauh, jarak)
        print(f"Tarif penumpang: Rp{tarif:,.0f}".replace(",", "."))
        print("\n--- Ringkasan ---")
        print(f"Jumlah penumpang : {jumlah_penumpang}")
        print(f"Total pendapatan : Rp{total_pendapatan:,.0f}".replace(",", "."))
        if jumlah_penumpang > 0:
            rata_rata_jarak = total_jarak / jumlah_penumpang
            print(f"Jarak terjauh    : {jarak_terjauh} km")
            print(f"Rata-rata jarak  : {rata_rata_jarak:.2f} km")
        else:
            print("Belum ada penumpang.")