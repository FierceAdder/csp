import pickle

def add_record():
    F=open("shoes.dat", "ab")
    s_id = int(input("Enter shoe ID: "))
    name = input("Enter shoe name: ")
    brand = input("Enter shoe brand: ")
    type = input("Enter shoe type: ")
    price = float(input("Enter shoe price: "))
    shoe = [s_id, name, brand, type, price]
    pickle.dump(shoe, F)
    print("Record added successfully!")

def display_records():
    F=open("shoes.dat", "rb")
    try:
        while True:
            shoe = pickle.load(F)
            print("Shoe ID:", shoe[0])
            print("Name:", shoe[1])
            print("Brand:", shoe[2])
            print("Type:", shoe[3])
            print("Price:", shoe[4])
            print("--------------------")
    except EOFError:
        pass  # End of file reached

def search_record():
    search_id = int(input("Enter shoe ID to search: "))
    found = False
    F=open("shoes.dat", "rb")
    try:
        while True:
            shoe = pickle.load(F)
            if shoe[0] == search_id:
                print("Record found:")
                print("Shoe ID:", shoe[0])
                print("Name:", shoe[1])
                print("Brand:", shoe[2])
                print("Type:", shoe[3])
                print("Price:", shoe[4])
                found = True
                break
    except EOFError:
        pass
    if not found:
        print("Record not found!")

while True:
    print("\nMenu:")
    print("1. Add record")
    print("2. Display records")
    print("3. Search record")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        display_records()
    elif choice == "3":
        search_record()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")

print("Exiting program...")
