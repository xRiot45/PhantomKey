from menu import menu
from encryption import encryption


def encrypt_menu():
    print("")
    print("============ CHOOSE ENCRYPTION TYPE ============")
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
        encryption.md2_encrypt()
    elif option == "2":
        encryption.md4_encrypt()
    elif option == "3":
        encryption.md5_encrypt()
    elif option == "4":
        encryption.sha1_encrypt()
    elif option == "5":
        encryption.sha256_encrypt()
    elif option == "6":
        encryption.sha512_encrypt()
    elif option == "7":
        encryption.bcrypt_encrypt()
    elif option == "b":
        menu.main_menu()
    elif option == "e":
        print("Goodbye!")
    else:
        print("Invalid option!")
        encrypt_menu()
