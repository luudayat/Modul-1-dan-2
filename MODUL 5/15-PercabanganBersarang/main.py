# percabangan Bersarang / nested IF

# kalkulator
# +,-,x,/,mod,//,pangkat(expone)

print(20*"=")
print("kalkulator sederhana")
print(20*"=")

angka_1 = float(input("masukkan bilangan 1 = "))
operator = input("operator (+,-,/,x,%,//,**) = ")
angka_2 = float(input("masukkan bilangan 2 = "))

# percabangan bersarang (elif statement)

if operator == '+' :
    hasil = angka_1 + angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '-' :
    hasil = angka_1 - angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == 'x' or operator == '*' :
    hasil = angka_1 * angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '/' :
    hasil = angka_1 / angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '%' or operator == 'mod' :
    hasil = angka_1 % angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '//' :
    hasil = angka_1 // angka_2
    print(f'hasilnya adalah = {hasil}')
elif operator == '**' :
    hasil = angka_1 ** angka_2
    print(f'hasilnya adalah = {hasil}')