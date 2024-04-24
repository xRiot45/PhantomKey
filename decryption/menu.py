from menu import menu
from decryption import decryption


def decrypt_menu():
    print("============ CHOOSE DECRYPTION TYPE ============")
    print("[1] MD2")
    print("[2] MD4")
    print("[3] MD5")
    print("[4] SHA-1")
    print("[5] SHA-256")
    print("[6] SHA-512")
    print("[7] Bcrypt")
    print("[b] Back")
    print("[e] Exit")

    print("")
    option = input("Enter a option: ")
    print("")

    if option == "1":
        decryption.md2_decrypt()
    elif option == "2":
        print("MD4")
    elif option == "3":
        print("MD5")
    elif option == "4":
        print("SHA-1")
    elif option == "5":
        print("SHA-256")
    elif option == "6":
        print("SHA-512")
    elif option == "7":
        print("Bcrypt")
    elif option == "b":
        menu.main_menu()
    elif option == "e":
        print("Goodbye!")
    else:
        print("Invalid option")
