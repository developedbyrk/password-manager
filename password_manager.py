import os

def add():
    name = input("Enter username: ").strip()
    pwd = input("Enter password: ").strip()

    with open("password.txt", "a") as f:
        f.write(f"{name}|{pwd}\n")

def view_all():
    if not os.path.exists("password.txt"):
        print("No saved passwords found. Please add a password first.")
        return

    with open("password.txt", 'r') as f:
        all_saved_password = f.read()
        print(all_saved_password)

def find_one(user):
    if not os.path.exists("password.txt"):
        print("No saved passwords found. Please add a password first.")
        return

    found = False
    with open("password.txt", 'r') as f:
        for line in f:
            name_pass = line.rstrip().split("|")
            if user == name_pass[0]:
                print(f"Your password is {name_pass[1]}")
                found = True
                break
    if not found:
        print("Username not found.")


while True:
    mode = input("Choose an option: add, view, find (q to quit): ").lower()
    if mode == 'q':
        break

    if mode == 'add':
        add()
    elif mode == 'view':
        view_all()
    elif mode == 'find':
        user = input("Enter your username to get the password: ")
        find_one(user)
    else: 
        print("Invalid selection")
        continue