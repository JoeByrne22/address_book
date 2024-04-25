import sqlite3

con = sqlite3.connect("address_book.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS address_book (name TEXT, email TEXT, address TEXT)")

class AddressBookInterface:
    def __init__(self, name):
        self.name = name
        self.object_list = []

    def __repr__(self):
        return f"AddressBookInterface({self.name})"

    def display_menu(self):
        print("1. Add person")
        print("2. View address book")
        print("3. Exit")

    def add_address(self):
        name = input("Enter name: ")
        email = input("Enter email: ") 
        address = input("Enter address: ")  
        cur.execute("INSERT INTO address_book (name, email, address) VALUES (?, ?, ?)", (name, email, address))
        con.commit() 
        new_object = AddressBookInterface(name)
        new_object.email = email
        new_object.address = address
        self.object_list.append(new_object)

    def view_contact(self):
        print("view_contact")
        cur.execute("SELECT name, email, address FROM address_book")
        for row in cur.fetchall():
            print(f"Name: {row[0]}, Email: {row[1]}, Address: {row[2]}")

    def exit_address_book(self):
        con.close()
        print("SEE YA")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_address()
            elif choice == '2':
                self.view_contact()
            elif choice == '3':
                self.exit_address_book()
                break