from . import Database
def read():
    try:
        with open(Database.DB_NAME,'r') as file:
            content = file.readlines()
            print(content)
            return content
    except:
        print("Membaca Database Error")
        return False