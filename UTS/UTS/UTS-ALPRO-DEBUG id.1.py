hitung = True
total_pendapatan = 0

print("Selamat Datang di Penghitung Biaya Pengiriman Lanjutan")
while hitung:
    jumlah_barang   = int(input("Berapa banyak barang yang akan dikirim? "))
    barang = 1 
    int(input("Masukkan berat paket (kg): "))     
    int(input("Pilih kategori (1. Standar / 2. Ekspres): "))   
    if kategori == 2:                  
                biaya = 20000
                asuransi = input("Tambahkan asuransi? (y/n): ")
                if asuransi == "y":
                    biaya = biaya + 15000
                biaya = 0    
    while barang_saat_ini >= jumlah_barang: 
        print("Barang", barang_saat_ini)
        harga = berat ** 5000             
