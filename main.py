"""
Main script to manage passwords using Fernet encryption.

The user can:
- Add new passwords
- View stored passwords
- Delete existing passwords
"""

from FernetClass import FernetClass

def main():
    # Create an instance of FernetClass
    cf = FernetClass()
    # Generate or load the encryption key
    cf.generate_fer()

    # Loop until the user provides a valid master username
    while True:
        master_user = input("Enter the name of the master user ==> ").strip()
        if master_user == "":
            print("The master password cannot be empty")
        else:
            break

    # Main loop to handle user commands
    while True:
        user_answer = input("Hello, what do you want to do inside the program? Add? View? Delete? If you want to exit, press q ==> ").lower()
        if user_answer == "add":
            # Add a new password entry
            cf.add(master_user)
        elif user_answer == "view":
            # View all passwords associated with the master user
            cf.view(master_user)
        elif user_answer == "delete":
            # Delete a password for the master user
            cf.delete_psw(master_user)
        elif user_answer == "q":
            # Exit the program
            quit()
        else:
            # Handle invalid commands
            print("Please write Add / View / Delete / q, otherwise I cannot proceed")

# Start the program
main()
