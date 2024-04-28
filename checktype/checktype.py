import time
import fade
from menu import menu
from banner import banner_color
from option.option import get_user_option


def checktype_hash():
    print("")
    print("============ CHECK TYPE HASH ============")
    text = input("Input the hash password for check the type: ").lower().strip()

    # MD2 , MD4 , MD5
    if len(text) == 32:
        print("Checking type hash.", end="", flush=True)
        for i in range(5):
            time.sleep(1)
            print(".", end="", flush=True)

        print("\n")
        print(f"{text} ==>> " + fade.greenblue("MD2, MD4, MD5"))

    # SHA-1
    elif len(text) == 40:
        print("Checking type hash.", end="", flush=True)
        for i in range(5):
            time.sleep(1)
            print(".", end="", flush=True)

        print("\n")
        print(f"{text} ==>> " + fade.greenblue("SHA-1"))

    # SHA-256
    elif len(text) == 64:
        print("Checking type hash.", end="", flush=True)
        for i in range(5):
            time.sleep(1)
            print(".", end="", flush=True)

        print("\n")
        print(f"{text} ==>> " + fade.greenblue("SHA-256"))

    # SHA-512
    elif len(text) == 128:
        print("Checking type hash.", end="", flush=True)
        for i in range(5):
            time.sleep(1)
            print(".", end="", flush=True)

        print("\n")
        print(f"{text} ==>> " + fade.greenblue("SHA-512"))

    # Bcrypt
    elif len(text) == 60:
        print("Checking type hash.", end="", flush=True)
        for i in range(5):
            time.sleep(1)
            print(".", end="", flush=True)

        print("\n")
        print(f"{text} ==>> " + fade.greenblue("Bcrypt"))
    else:
        print("Checking type hash.", end="", flush=True)
        for i in range(5):
            time.sleep(1)
            print(".", end="", flush=True)

        print("\n")
        print(f"{text} ==>> " + fade.greenblue("Unknown hash type!"))

    option = get_user_option()
    if option == "y":
        checktype_hash()
    elif option == "n":
        print(banner_color)
        menu.main_menu()
    else:
        option = get_user_option()
