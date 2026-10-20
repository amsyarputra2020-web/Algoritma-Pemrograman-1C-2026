pin = int(input("Masukkan 3 digit PIN           : "))
jam = int(input("Masukkan jam kedatangan (0-23) : "))
digit_pertama = pin // 100
digit_kedua   = (pin // 10) % 10
digit_ketiga = pin % 10
if pin % 5 == 0:
    if jam < 12:
        status_akses = ("Garasi Pagi Terbuka")
    else:
        status_akses = ("Garasi Malam Terbuka, Lampu Dinyalakan")
elif pin % 2 == 0:
    if (digit_pertama + digit_ketiga) == digit_kedua:
        status_akses = ("Garasi VIP Terbuka Khusus Bos")
    else:
        status_akses = ("Kode Genap Ditolak, Alarm Berbunyi!")
else:
    status_akses = ("Akses ditolak sepenuhnya")
if jam > 18:
    status_kamera = ("Mode Malam Merekam")
else:
    status_kamera = ("Mode Siang Standby")
print("Digit PIN                      :", digit_pertama,digit_kedua,digit_ketiga)
print("Status Akses                   :", status_akses)
print("Status Kamera                  :", status_kamera)