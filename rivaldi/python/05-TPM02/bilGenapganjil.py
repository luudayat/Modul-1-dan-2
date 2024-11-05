def cek_ganjil_genap():
    try:
        bilangan = int(input("Masukkan sebuah bilangan: "))
        
        if bilangan % 2 == 0:
            print(f"{bilangan} adalah bilangan genap.")
        else:
            print(f"{bilangan} adalah bilangan ganjil.")
    except ValueError:
        print("Input tidak valid! Harap masukkan bilangan bulat.")

if __name__ == "__main__":
    cek_ganjil_genap()