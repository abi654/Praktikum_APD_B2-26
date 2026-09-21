skincare_1 = 35000
skincare_2 = 42000
skincare_3 = 50000
skincare_4 = 55000
skincare_5 = 68000
skincare_6 = 70000

harga_skincare = [skincare_1, skincare_2, skincare_3, skincare_4, skincare_5, skincare_6]

total_pengeluaran = skincare_1 + skincare_2 + skincare_3 + skincare_4 + skincare_5 + skincare_6 + 12000
rata_rata = total_pengeluaran / len(harga_skincare)
nim = 63
bolean = nim < rata_rata

kurs_jpy = 1.0875
total_jpy = total_pengeluaran * kurs_jpy
slice_3_sampai_5 = harga_skincare[-4:-1]

print(skincare_1, skincare_2, skincare_3, skincare_4, skincare_5, skincare_6)
print(harga_skincare)
print(total_pengeluaran)
print(rata_rata)
print(nim)
print(bolean)
print(total_jpy)
print(slice_3_sampai_5)