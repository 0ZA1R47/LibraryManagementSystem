from ast import Pass
from pickle import POP
import sqlite3 as db
import pyfiglet as pyf
import os
from getpass import getpass
import time 

# Display Message Function 
def display_message():
        banner = pyf.figlet_format("Air University Library Management System")
        print(banner)
        print("--------------------------------------------------------")
        
        print("[+] Please Login to proceed further")
        time.sleep(1)
        os.system('clear')

# Dictionary for books 
BooksDB = { 

} 

# Function to Add books in the Database 
def Add_Books():

    user_choice = 'y'
    while (user_choice == 'y' or user_choice=='Y'):
        B_ID = input("> Book ID = ")
        B_title = input("> Title = ")
        B_price = input("> Price = ")
        B_author = input("> Author = ")
        B_year = input("> Year of Publish =")
        B_quantity = input("> Quantity = ")
        flag = False
        for i in BooksDB:
            if i == B_ID:
                flag = True
                print(f"{B_ID} already exists")
            continue
        else: 
            BooksDB[B_ID] = {'title': B_title, 'price': B_price, 'author': B_author, 'year':B_year,'Quantity': B_quantity}
            print(f"[+] Book {B_title} sucessfully added! ")
       
        user_choice = input("[-] Want to add more books or exit? (Y/N) ")
   
    revisit_menu = input("[-] Want to revisit the main menu? (Y/N)")
    if (revisit_menu == 'y' or revisit_menu == 'Y'):
        admin_menu()
    
# Function to edit books
def Edit_Books():
    pass

# Function to delete books 
def Delete_Books():
    user_choice = "y"
    
    while (user_choice == "y" or user_choice == "Y"):
        rmv_ID = input("> Please enter the Book ID: ")
        book_list = list(BooksDB)
      
        if len(book_list) > 0:
            for key in book_list:
                if  key != rmv_ID:
                    print(f"[-] Book ID: {rmv_ID} doesn't exits! ")
                else:
                    BooksDB.pop(rmv_ID)
                    print(f"[-] Book ID: {rmv_ID} deleted!")    
        else:
            print("[-] No books exists!")

        user_choice = input("Want to delete more books or exit (Y/N)")
   
    revisit_menu = input("[-] Want to revisit the main menu? (Y/N)")
    if (revisit_menu == 'y' or revisit_menu == 'Y'):
        admin_menu()
    

# Function to view books in the Database
def View_Books():
    for book_id, book_info in BooksDB.items():
        print("Book ID:", book_id)
    
        for key in book_info:
            print(key + ':', book_info[key])
        print("\n")

# Function to purchase books 
def Purchase_Books():
    pass

# Function for User Menu
def user_menu():
    banner = pyf.figlet_format("User Dashboard")
    print(banner)
    
    print("[+] 1. View Books\n[+] 2. Purchase Books")
    user_choice = input("Please select an option to proceed further: ")
    
    if user_choice == "1":
        View_Books()
    
    elif user_choice == "2":
        Purchase_Books()

# Function for Admin Menu
def admin_menu():
    banner = pyf.figlet_format("Admin Dashboard")
    print(banner)


    print("[+] 1. Add Books\n[+] 2. Delete Books\n[+] 3. Edit Books\n[+] 4. View Books")
    
    admin_choice = input("Please select an option to proceed further: ")
    
    if admin_choice == "1":
        Add_Books()

    elif admin_choice == "2":
        Delete_Books()
        
    elif admin_choice == "3":
        Edit_Books()

    elif admin_choice == "4": 
        View_Books()

    else:
        print("[-] Please choose correct option!")

# Function for user and admin login
def login():
   
    admin_username = "Ozair"
    admin_password = "test1"

    user_name = "Ozair"
    user_password = "test2"

    username = input("Username = ")
    password = getpass("Password = ")

    time.sleep(1)
    os.system('clear')

    if username == admin_username and password == admin_password:
        admin_menu()
    
    elif username == user_name and password == user_password:
        user_menu()
    else: 
        print("[-] Please enter valid credentials!")
        login()

# Main function 
if __name__=="__main__":
    display_message()
    login()
