from banner import banner_color
from menu import menu
from hashing import hashing


def hashing_menu():
    print("")
    print("============ CHOOSE TYPE HASHING ============")
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
        hashing.md2_hashing()
    elif option == "2":
        hashing.md4_hashing()
    elif option == "3":
        hashing.md5_hashing()
    elif option == "4":
        hashing.sha1_hashing()
    elif option == "5":
        hashing.sha256_hashing()
    elif option == "6":
        hashing.sha512_hashing()
    elif option == "7":
        hashing.bcrypt_hashing()
    elif option == "b":
        print(banner_color)
        menu.main_menu()
    elif option == "e":
        print("Goodbye!")
    else:
        print("Invalid option!")
        hashing_menu()
