# 🔐 Simple Password Manager (CLI)

A beginner-friendly Python command-line application to store and retrieve passwords using basic file handling.

---

## 📦 Features

- Add new username and password pairs
- View all saved credentials
- Find and display the password for a specific username
- File-based storage using `password.txt`
- Simple text-based interface for learning fundamentals

---

## 🛠 Requirements

- Python 3.x
- No external libraries required (uses only built-in modules)

---

## 🚀 How to Use

1. **Run the program:**

   ```bash
   python password_manager.py

2. **Follow the prompts:**

   Choose an option: add, view, find (q to quit):

2. **Options:**

      add – Add a new username and password

      view – View all saved credentials

      find – Retrieve the password for a specific username

      q – Quit the program

**Example:**

      Choose an option: add, view, find (q to quit): add

      Enter username: alice

      Enter password: mypassword123


      Choose an option: view, add, find (q to quit): view

      alice|mypassword123


      Choose an option: find

      Enter your username to get the password: alice

      Your password is mypassword123




