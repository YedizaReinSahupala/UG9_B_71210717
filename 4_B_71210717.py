print("=====GEBYAR DISKON=====")
print("=====MASUKAN JUMLAH BARANG YANG DIPESAN=====")

#KIPAS ANGIN= x
#SEPEDA = y
#HELM ROSSI= z
#t=total diskon masing-masing barang


x= int(input("KIPAS ANGIN DISKON 10%   Rp 25.000,00   : "))
y= int(input("SEPEDA DISKON 55%        Rp 6.000,00    : "))
z= int(input("HELM ROSSI DISKON 77%    Rp 8.000,00    : "))

print("=====TOTAL=====")

tx= 25000 * x * 10/100
ty= 6000 * y * 55/100
tz= 8000 * z * 77/100

print("TOTAL KIPAS ANGIN     : Rp ", tx)
print("TOTAL SEPEDA SUPER    : Rp ", ty)
print("TOTAL HELM ROSSI      : Rp ", tx)

Total_diskon= tx + ty + tz

print("Jumlah total diskon yang didapat adalah Rp", Total_diskon)

