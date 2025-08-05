# 🔐 Python Password Manager

This project is a simple **password manager** developed in Python.  
It allows you to securely store, view, and delete passwords using **symmetric encryption** via the [Fernet](https://cryptography.io/en/latest/fernet/) module.  
Passwords are encrypted and stored locally in a text file, while the encryption key is managed in a separate file.

---

## 🚀 Features

✅ Add encrypted passwords associated with a master user  
✅ View all stored passwords for a given master user  
✅ Delete specific passwords with confirmation prompts  
✅ Auto-generates the encryption key file if it does not exist  
✅ Input masking for password entry  

---

## 📂 Project Structure

- **main.py** – Main script to start the game
- **FernetClass.py** – Class handling encryption, storage, and deletion logic
- **File_key.key** - (Auto-generated) encryption key
- **Password.txt** - (Auto-generated) encrypted password storage
- **README.md** - Project documentation

---

## ⚙️ Requirements

- Python 3.x
- cryptography library

You can install the required library via: pip install cryptography

---

## 📬 Contact & Collaboration

For questions, suggestions, or collaborations on this or **other larger projects**, feel free to reach out:

📧 **luca.linari@gmail.com**

---

## 💡 How to Run 

1. Clone this repository at URL: https://github.com/LinariLuca/Password_Management.git
2. cd Password_Management-main
3. python main.py
4. Enjoy the project (in “Password.txt” there is already a user with a corresponding password)

---

## 📌 Future work / possible improvements

1. Define that when a user enters a password, it must have a certain minimum length and certain special characters (e.g. oblige user to have at least one character such as ! or # and at least one capital letter)
2. Store data in a SQLite encrypted database instead of plain text
3. Create a GUI with Tkinter



