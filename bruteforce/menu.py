from menu import menu
from bruteforce import bruteforce


def bruteforce_menu():
    print("============ CHOOSE TYPE HASHING FOR BRUTE FORCE ============")
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
        bruteforce.md2_bruteforce()
    elif option == "2":
        bruteforce.md4_bruteforce()
    elif option == "3":
        bruteforce.md5_bruteforce()
    elif option == "4":
        bruteforce.sha1_brueforce()
    elif option == "5":
        bruteforce.sha256_bruteforce()
    elif option == "6":
        bruteforce.sha512_bruteforce()
    elif option == "7":
        print("Bcrypt")
    elif option == "b":
        menu.main_menu()
    elif option == "e":
        print("Goodbye!")
    else:
        print("Invalid option")
