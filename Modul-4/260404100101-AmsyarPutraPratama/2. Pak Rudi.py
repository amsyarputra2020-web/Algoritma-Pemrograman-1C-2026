gaji_pokok = 100000
total_gaji = 0
for hari in range(1, 8) :
    print("\nHari ke -", hari)
    lembur = int(input("Masukkan lama lembur : "))
    while lembur not in [0,1,2,3,4,6,8]:
        print ("Diluar konteks woy")
        lembur = int(input("Masukkin lagi : "))
    total_gaji = total_gaji + gaji_pokok
    if lembur >=1 and lembur <= 3 :
        upah_lembur = lembur * 25000
        total_gaji = total_gaji + upah_lembur
        print ("Total sementara      :",total_gaji)
    elif lembur == 4 :
        upah_lembur = 100000
        total_gaji = total_gaji + upah_lembur
        print ("Total sementara      :",total_gaji)
    elif lembur == 6 :
        upah_lembur = 200000
        total_gaji = total_gaji + upah_lembur
        print ("Total sementara      :",total_gaji)
    elif lembur == 8 :
        upah_lembur = 300000
        total_gaji = total_gaji + upah_lembur
        print ("Total sementara      :",total_gaji)

shift_malam = input("\nShift malam kah? ")
if shift_malam in ["Yoi","Y","y","Yut","Hooh","Iya"] :
    total_gaji = total_gaji + 50000
    print("Selamat dapet bonus (cmiww)")
    print("Total gaji :",total_gaji)
else :
    print("Yek boty")