# menuntukan BMI
berat_badan = float(input('masukan berat badan (kg):'))
tinggi_badan = float(input('masukan tinggi badan (m)'))

tinggi_badan = tinggi_badan / 100
bmi = berat_badan / (tinggi_badan ** 2)

# menentukan hasil 
print (f'nilai BMI anda adalah: {bmi:.1f}')

 