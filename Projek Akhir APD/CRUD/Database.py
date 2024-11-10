DB_NAME = "data.txt"

def init_console():
    try:
        with open("data.txt, "r"") as file:
            print("Database tersedia, init done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        with open("data.txt","w",encoding="utf-8") as file:
            nama = input("Nama Pelanggan: ")
            makanan = input ("Makanan yang dipesan: ")
            minuman = input("Minuman yang dipesan: ")
            data_str = f"{nama},{makanan},{minuman}"
            file.write(data_str)