import os
import CRUD as CRUD

def clear():
    os.system("cls")

if __name__ == "__menu__":
    sistem_operasi = os.name
clear()
print("Selamat datang di E-Garlip Kami")
print("Database E-GARLIP")
print("==========================")

#check database
CRUD.init_console()

while True:
    clear()
    print("Selamat datang di E-Garlip Kami")
    print("Database E-GARLIP")
    print("==========================")

    print("1.Read Data")
    print("2.Create Data")
    print("3.Edit Data")
    print("4.Delete Data")
    print("==========================")

    
    user_option = input("Masukkan angka: ")
    
    match user_option:
        case "1": CRUD.read_console()
        case "2":
            print("Create Data")
        case "3":
            print("Update Data")
        case "4":
            print("Delete Data")
    
    is_done = input("Apakah Selesai?")
    if is_done == "y" or is_done == "Y":
        break
print("Program Selesai")