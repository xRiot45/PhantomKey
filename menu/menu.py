from encryption import menu as encrypt
from decryption import menu as decrypt


def main_menu():
    print("Welcome to PhantomKey, the encryption and decryption tool.")
    print("Version      : 1.0")
    print("Developed by : xRiot")
    print("")
    print("============ CHOOSE A OPTION ============")
    print("[1] Encrypt")
    print("[2] Decrypt")
    print("[e] Exit")

    print("")
    option = input("Enter a option: ")

    if option == "1":
        encrypt.encrypt_menu()
    elif option == "2":
        decrypt.decrypt_menu()
    elif option == "e":
        print("Goodbye!")
    else:
        print("Invalid option!")
        main_menu()
