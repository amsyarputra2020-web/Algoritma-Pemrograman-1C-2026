baris = int(input("Masukkan jumlah baris : "))
lampu = int(input("Masukkan jumlah lampu : "))

for baris in range (1, baris+1):
    for lampu in range (1, lampu+1):
        if lampu % 3 == 0:
            print(f"Baris {baris}, Lampu {lampu}: Gangguan")
        else :
            print(f"Baris {baris}, Lampu {lampu}: Normal")
print("\nPeriksa sumber listrik utama taman.")