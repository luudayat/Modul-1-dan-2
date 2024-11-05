def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) * 32
def fahrenheit_ke_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("kenversi Suhu")
    print("1. celcius ke fahrenheit")
    print("2. fahrenheit ke celcius")
    pilihan = input("pilihan (1/2): ")
    if pilihan == '1':
        celcius = float(input("masukan suhu dalam celcius : "))
        fahrenheit = celcius_ke_fahrenheit(celcius)
        print(f"{celcius}C = {fahrenheit}F")
    elif pilihan == '2':
        fahrenheit = float(input("masukan suhu dalam fahrenheit: "))
        celcius = fahrenheit_ke_celcius(fahrenheit)
        print(f"{fahrenheit}F = {celcius}C")
    else:
        print("pilihan tifak valid!")

if __name__ == "__main__": main()   
            
        