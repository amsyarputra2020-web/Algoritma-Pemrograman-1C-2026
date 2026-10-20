jarak_satu_arah_km     = 100
konsumsi_km_per_liter  = 40
sisa_bahan_bakar_liter = 1.5
harga_per_liter_rupiah = 10000

jarak_pulang_pergi_km         = jarak_satu_arah_km*2
kebutuhan_bahan_bakar_liter   = jarak_pulang_pergi_km/konsumsi_km_per_liter
bahan_bakar_yang_dibeli_liter = max(kebutuhan_bahan_bakar_liter - sisa_bahan_bakar_liter,0,)
total_biaya_rupiah            = bahan_bakar_yang_dibeli_liter * harga_per_liter_rupiah

print(f"Jarak pulang-pergi            : {jarak_pulang_pergi_km:g} km")
print(f"Kebutuhan bahan bakar         : {kebutuhan_bahan_bakar_liter:g} liter")
print(f"Bahan bakar yang perlu dibeli : {bahan_bakar_yang_dibeli_liter:g} liter")
print(f"Total biaya                   : Rp{total_biaya_rupiah:,.0f}".replace(",", "."))