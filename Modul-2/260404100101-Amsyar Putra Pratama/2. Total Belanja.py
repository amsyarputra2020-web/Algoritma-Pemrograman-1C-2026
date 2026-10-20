total_belanja = int(input("Masukkan total belanja : "))
if total_belanja % 100000 == 0:
    print("Gratis")
elif total_belanja % 50000 == 0:
    print("Dapat diskon 50% jadi  :",total_belanja - total_belanja * 50/100)
elif total_belanja % 10000 == 0:
    print("Dapat diskon 20% jadi  :",total_belanja - total_belanja * 20/100)
elif total_belanja >= 200000 :
    print("Dapat diskon 10% jadi  :",total_belanja - total_belanja*10/100)
else:
    print("Bayar normal ya :)")
status_poin = ("Poin Bertambah") if total_belanja > 0 else "Tidak Ada Poin"
print(f"Status poin            : {status_poin}")