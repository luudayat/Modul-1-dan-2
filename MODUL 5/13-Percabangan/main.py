# percabangan
# struktur
"""
   1. if -nya
   2. punya kondisi
   3. punya aksi
"""
nama = input("Masukkan nama :")

# percabangan yang inline (satu baris)
#if nama == "Ramadhana" : print("Selamat datang")
#print("Terima kasih")

# percabangan indentasi
#if nama == "ramadhan":
#   print("selamat Datang")
#    print("Selamat Belajar python")
#print("Buka Bagian Percabangan")

# percabangan 1 kondisi dan 2 aksi
# pakai kata kunci 'alse'

if nama == "ramadhan":
    print("selamat Datang")
else:
    print(f'anda (nama), bukan ramadhan')
print("Terima kasih")