from encryption import menu as encrypt
from bruteforce import menu as bruteforce


def main_menu():
    print("Welcome to PhantomKey, the hashing and brute force tool.")
    print("Version      : 1.0")
    print("Developed by : xRiot")
    print("")
    print("============ CHOOSE A OPTION ============")
    print("[1] Hashing")
    print("[2] Brute Force")
    print("[e] Exit")

    print("")
    option = input("Enter a option: ")

    if option == "1":
        encrypt.encrypt_menu()
    elif option == "2":
        bruteforce.bruteforce_menu()
    elif option == "e":
        print("Goodbye!")
    else:
        print("Invalid option!")
        main_menu()
