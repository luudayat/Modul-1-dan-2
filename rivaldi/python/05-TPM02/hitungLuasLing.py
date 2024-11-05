import math

#minta input dari pengguna untuk jari jari lingkaran
radius = float(input("masukkan jari-jari lingkaran : "))

#menghitung luas lingkaran
area = math.pi * radius ** 2

#menampilkan hasil
print(f"luas lingkaran dengan jari-jari {radius} adalah {area:.2f}")