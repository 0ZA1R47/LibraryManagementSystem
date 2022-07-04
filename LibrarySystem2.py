from cmath import pi
from curses.panel import new_panel
import sqlite3 as db
import pyfiglet as pyf
import os
from getpass import getpass
import time 

# Connecting Database 
def connect_db(): 
    global db_conn 
    db_conn = db.connect('books.db')
    global cursor 
    cursor = db_conn.cursor()

# Commiting changes and closing database connection 
def close_db():
    db_conn.commit()
    db_conn.close()
    
# Creat Table Books
def create_table():
    create_table = '''create table if not exists books (Id INTEGER PRIMARY KEY NOT NULL, 
                                                    title TEXT NOT NULL,
                                                    price FLOAT NOT NULL,
                                                    author TEXT NOT NULL,
                                                    year INTEGER NOT NULL,
                                                    quantity INTEGER NOT NULL)'''
    cursor.execute(create_table)
    db_conn.commit()

# Clear screen function 
def clr_scr():
    time.sleep(1)
    os.system('clear')
        
# Display Message Function 
def display_message():
    banner = pyf.figlet_format("Air University Library Management System")
    print(banner)
    print("--------------------------------------------------------")
        
    print("[+] Please Login to proceed further")
    clr_scr()

# Function to Add books in the Database 
def Add_Books():
    create_table()
    
    user_choice = 'y'
    while (user_choice == 'y' or user_choice=='Y'):
        print("[+] Please enter the following information of the book:\n ")
        Id = input("> Book ID = ")
        title = input("> Title = ")
        price = input("> Price = ")
        author = input("> Author = ")
        year = input("> Year of Publish =")
        quantity = input("> Quantity = ")
        
        values = (int(Id), title, float(price), author, int(year), int(quantity))
        Input_values = '''INSERT INTO books values (?, ?, ?, ?, ?, ?) '''
        cursor.execute(Input_values, values)
        db_conn.commit()

        user_choice = input("[-] Want to add more books or exit? (Y/N): ")

    revisit_menu = input("[-] Want to revisit the main menu? (Y/N)")
    if (revisit_menu == 'y' or revisit_menu == 'Y'):
        admin_menu()
    

# Function to edit books
def Edit_Books():

    user_choice = "y"
    
    while (user_choice == "y" or user_choice == "Y"):
        Edit_Id = input("> Please enter the Book ID to edit: ")
        print("[+] 1. Edit title\n[+] 2. Edit price\n[+] 3. Edit author\n[+] 4. Edit year\n[+] 5. Edit quantity")
        menu_choice = input("[+] Please select an option to proceed further: ")
        
        if menu_choice == "1": 
            new_title = input("> Enter new title: ")
            print(new_title)
            print(Edit_Id)
            querry = "UPDATE books SET title = '{0}' WHERE '{1}'".format(new_title, Edit_Id )
            cursor.execute(querry)
            db_conn.commit()
        elif menu_choice == "2": 
            new_price = input("> Enter new price: ")
            cursor.execute(f"UPDATE books SET price = {float(new_price)} WHERE Id = {int(Edit_Id)}")
            db_conn.commit()
        elif menu_choice == "3": 
            new_author= input("> Enter new author: ")
            cursor.execute(f"UPDATE books SET author = {new_author} WHERE Id = {int(Edit_Id)}")
            db_conn.commit()
        elif menu_choice == "4": 
            new_year= input("> Enter new year: ")
            cursor.execute(f"UPDATE books SET year = {int(new_year)} WHERE Id = {int(Edit_Id)}")
            db_conn.commit()
        elif menu_choice == "5": 
            new_quantity = input("> Enter new quantity: ")
            cursor.execute(f"UPDATE books set price = {int(new_quantity)} WHERE Id = {int(Edit_Id)}")
            db_conn.commit()
        else:
            print("[-] Please select correct option!")
            Edit_Books()

        user_choice = input("Want to edit more books or exit (Y/N)")
   
    revisit_menu = input("[-] Want to revisit the main menu? (Y/N)")
    if (revisit_menu == 'y' or revisit_menu == 'Y'):
        admin_menu()
   
    

# Function to delete books 
def Delete_Books():
    user_choice = "y"
    
    while (user_choice == "y" or user_choice == "Y"):
        rmv_Id = input ("> Please enter the Book ID to delete: ")
        cursor.execute(f"SELECT Id FROM books WHERE Id = {rmv_Id}")

        if rmv_Id in cursor:
             cursor.execute(f"DELETE FROM  books where Id = {rmv_Id}")
             db_conn.commit()
             print(f"[-] Book ID: {rmv_Id} Deleted!!")
        else:
            print(f"[-] Book ID: {rmv_Id} does not exist! ")

        user_choice = input("Want to delete more books or exit (Y/N)")
   
    revisit_menu = input("[-] Want to revisit the main menu? (Y/N)")
    if (revisit_menu == 'y' or revisit_menu == 'Y'):
        admin_menu()
    

# Function to view books in the Database
def View_Books():
    print("[-] Below are the books currently available in the Database: ")
    cursor.execute("SELECT * FROM books ")
    for row in cursor:
        print(f"Book ID: {row[0]}")
        print(f"Title: {row[1]}")
        print(f"Price: {row[2]}")
        print(f"Author: {row[3]}")
        print(f"Year of Publish: {row[4]}")
        print(f"Quantity: {row[5]}")
        print("\n")
    
    '''revisit_menu = input("[-] Want to revisit the main menu? (Y/N)")
    if (revisit_menu == 'y' or revisit_menu == 'Y'):
        admin_menu()'''
    



# Function to purchase books 
def Purchase_Books():
    
    user_choice = "y"
    
    while (user_choice == "y" or user_choice == "Y"):
        View_Books()
        print("[+] Please select a book(s) from the available options:\n ")
        prchse_ID = input("> Please enter the Book ID to purchase the book(s): ")
        prchse_quantity = input("> Please enter the quantity:\n ")    

        cursor.execute(f"SELECT quantity FROM books where Id = {int(prchse_ID)}")
        for quantity in cursor:
            db_quantity = quantity[0]

        new_quantity = int(db_quantity) - int(prchse_quantity)

        if new_quantity <0:
            print("[-] OUT OF STOCK!! ")
        else:
            cursor.execute(f"UPDATE books set quantity = {int(new_quantity)} where Id = {int(prchse_ID)}")
            db_conn.commit()
            print("[+] Book Added to Cart! ")  

        user_choice = input("Want to purchase more books or exit (Y/N)")
        clr_scr()


# Function for User Menu
def user_menu():
    banner = pyf.figlet_format("User Dashboard")
    print(banner)
    
    print("[+] 1. Purchase Books")
    user_choice = input("> Please enter 1 to purchase books: ")
    
    if user_choice == "1":
        clr_scr()
        Purchase_Books()    
    else:
        print("[-] Please enter correct option!")
        user_menu()


# Function for Admin Menu
def admin_menu():
    banner = pyf.figlet_format("Admin Dashboard")
    print(banner)

    print("[+] 1. Add Books\n[+] 2. Delete Books\n[+] 3. Edit Books\n[+] 4. View Books")
    
    admin_choice = input("Please select an option to proceed further: ")
    
    if admin_choice == "1":
        clr_scr()
        Add_Books()
        
    elif admin_choice == "2":
        clr_scr()
        Delete_Books()
        
    elif admin_choice == "3":
        clr_scr()
        Edit_Books()

    elif admin_choice == "4": 
        clr_scr()
        View_Books()
    else:
        print("[-] Please choose correct option!")
        admin_menu()

# Function for user and admin login
def login():
   
    admin_username = "Ozair"
    admin_password = "test1"

    user_name = "Ozair"
    user_password = "test2"

    username = input("Username = ")
    password = getpass("Password = ")

    clr_scr()

    if username == admin_username and password == admin_password:
        admin_menu()
    
    elif username == user_name and password == user_password:
        user_menu()
    else: 
        print("[-] Please enter valid credentials!")
        login()

# Main function 
if __name__=="__main__":
    connect_db()
    display_message()
    login()
    close_db()

