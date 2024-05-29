from banner import banner_color
from menu import menu
from cracking import cracking


def cracking_menu():
    print("")
    print("============ CHOOSE TYPE HASHING FOR CRACKING ============")
    print("[1] MD2")
    print("[2] MD4")
    print("[3] MD5")
    print("[4] SHA-1")
    print("[5] SHA-256")
    print("[6] SHA-512")
    print("[7] Bcrypt ==>> | It takes a long time depending on the amount of salt |")
    print("[b] Back")
    print("[e] Exit")

    print("")
    option = input("Enter a option: ")
    print("")

    if option == "1":
        cracking.md2_cracking()
    elif option == "2":
        cracking.md4_cracking()
    elif option == "3":
        cracking.md5_cracking()
    elif option == "4":
        cracking.sha1_brueforce()
    elif option == "5":
        cracking.sha256_cracking()
    elif option == "6":
        cracking.sha512_cracking()
    elif option == "7":
        cracking.bcrypt_cracking()
    elif option == "b":
        print(banner_color)
        menu.main_menu()
    elif option == "e":
        print("Goodbye!")
    else:
        print("Invalid option")
