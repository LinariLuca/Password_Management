"""
FernetClass

This class provides secure password management using symmetric encryption (Fernet).
It allows adding, viewing, and deleting encrypted passwords stored in a text file.
"""

import os
import getpass as gp
from cryptography.fernet import Fernet

class FernetClass():

    def __init__(self):
        pass
        
    def generate_fer(self):
        # Generate a new Fernet key
        key = Fernet.generate_key()
        # Check if the key file already exists
        check_file = os.path.exists("File_key.key")
        key_file_main = ""
        
        if check_file:
            # If it exists, read the existing key from the file
            file = open("File_key.key", "rb")
            key_file_main = file.read()
            file.close()
        else:
            # If not, create the file and write the new key
            with open("File_key.key", "wb") as f:
                f.write(key)
            # Use the newly generated key
            key_file_main = key

        # Create the Fernet object using the key
        objFer = Fernet(key_file_main)
        return objFer

    def add(self, master_user):
        # Loop until valid (non-empty) input is provided
        while True:
            psw = gp.getpass("Inser password ==> ").strip()
            if master_user == "" or psw == "":
                print("Name or password cannot be empty, please enter valid strings")
            else:
                break

        # Create Fernet object to encrypt the password
        ferOBJ = self.generate_fer()
        with open("Password.txt", "a") as f:
            # Encrypt and save the password to file
            f.write(master_user + "|" + ferOBJ.encrypt(psw.encode()).decode() + "\n")
        
    def view(self, master_user):
        ferOBJ = self.generate_fer()
        count = 1
        trovato = False
        check_file_PSW = os.path.exists("Password.txt")

        if check_file_PSW:
            with open("Password.txt", "r") as f:
                for line in f.readlines():
                    # Remove any spaces/newlines
                    line_no_space = line.strip()
                    user, psw = line_no_space.split("|")
                    # Check if this entry matches the user
                    if user.lower() == master_user.lower():
                        print(f"{count}) User:", user, "|| Password:", ferOBJ.decrypt(psw.encode()).decode())
                        trovato = True
                        count += 1
                if not trovato:
                    print("No password found linked to this username")
        else:
            print("The file 'Password.txt' does not exist.")
            print("You can create it automatically using the 'Add' option to add the first password, or create an empty file named 'Password.txt'.")

    def delete_psw(self, master_user):
        objFER = self.generate_fer()
        count = 1

        if master_user == "":
            print("Cannot proceed: you did not enter the master user")
            quit()

        check_file_PSW = os.path.exists("Password.txt")
        if check_file_PSW:
            with open("Password.txt", "r") as f:
                lines = f.readlines()
        else:
            print("The file 'Password.txt' does not exist.")
            print("You can create it automatically using the 'Add' option to add the first password, or create an empty file named 'Password.txt'.")
            return

        lista_tuple = []  # List to collect (user, decrypted password) tuples

        check_psw_for_master_user = False
        for line in lines:
            str_senza_spazi = line.strip()
            user, psw = str_senza_spazi.split("|")

            # Check if the current line belongs to the specified user
            if master_user.lower() == user.lower():
                if not check_psw_for_master_user:
                    print("Passwords associated with user", master_user, "are:")
                    check_psw_for_master_user = True

                print(f"{count}) User:", user, "|| Password:", objFER.decrypt(psw.encode()).decode())
                count += 1
                # Save tuple of user and decrypted password
                lista_tuple.append((user, objFER.decrypt(psw.encode()).decode()))
                
        if not check_psw_for_master_user:
            print(f"No password found for user {master_user}")
            return
        
        # Ask which password to delete using getpass
        psw_to_delete = gp.getpass("After viewing the passwords, which one do you want to remove? Please enter it exactly: ")
        check_inside = False

        # Check if the provided password matches any stored ones
        for single_tupla in lista_tuple:
            if single_tupla[0] == master_user and single_tupla[1].strip() == psw_to_delete.strip():
                print("User", user, "wants to delete password:", psw_to_delete)
                check_inside = True
                check_while = True

                # Confirmation loop
                while check_while:
                    conferma_utente = input("Confirm deletion? This action is irreversible. Type y/n: ").lower()
                    if conferma_utente == "n":
                        print("Nothing has been deleted")
                        return
                    elif conferma_utente == "y":
                        # Rewrite the file excluding the selected password
                        with open("Password.txt", "w") as f:
                            for line in lines:
                                lineStrip = line.strip()
                                user_2, psw_2 = lineStrip.split("|")
                                # Skip the line to delete
                                if user_2 == master_user and psw_to_delete == objFER.decrypt(psw_2.encode()).decode():
                                    continue
                                f.write(line)
                        check_while = False
                        print("Deletion completed successfully")
                    else:
                        print("Please enter y or n to confirm")
        
        if not check_inside:
            print(f"No matching password found for user '{master_user}' with the specified password")
