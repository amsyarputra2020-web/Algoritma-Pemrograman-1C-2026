suhu = float(input("Masukkan suhu reaktor (°C): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))
if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        status = "Tekanan Tidak Stabil"
    else:
        status = "Operasi Reaktor Normal"
else:
    status = "Reaktor Belum Cukup Panas"
if suhu  > 800:
    print ("Pompa maksimal")
else :
    print ("Pompa normal")
pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"
print("\n=== STATUS REAKTOR ===")
print(f"Suhu     : {suhu} °C")
print(f"Tekanan  : {tekanan} Bar")
print(f"Status   : {status}")
print(f"Pompa    : {pompa}")