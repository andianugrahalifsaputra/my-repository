from . import Operasi
def read_console():
    data_file = Operasi.read()
    
    index_header = "No"
    nama_header = "Nama"
    makanan_header = "Nama Makanan"
    minuman_header = "Nama Minuman"

    #header
    print("\n" + "=" * 100)
    print(f"{index_header:4} | {nama_header:40} | {makanan_header:40} | {minuman_header:40}")
    print("-" * 100)
    
    #data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        
        # Pastikan jumlah data cukup
        if len(data_break) >= 3:
            nama = data_break[0]
            makanan = data_break[1]
            minuman = data_break[2]
            print(f"{index + 1:4} | {nama:40} | {makanan:40} | {minuman:40}")
        else:
            print(f"{index + 1:4} | Data tidak lengkap")

    print("=" * 100 + "\n")
