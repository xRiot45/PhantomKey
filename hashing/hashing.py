import time
import fade
import bcrypt
import hashlib
from hashing import menu
from option.option import get_user_option
from Crypto.Hash import MD2, MD4


# MD2 Hashing
def md2_hashing():
    print("============ MD2 ============")

    text = input("Enter the text to hashing: ").strip()
    text_encode = text.encode("utf-8")
    print("Hashing.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    hash_object = MD2.new()
    hash_object.update(text_encode)
    hashed_text = hash_object.hexdigest()

    print(f"\nMD2 =>> " + fade.greenblue(f" {hashed_text}"))

    print("")
    option = get_user_option()
    print("")

    if option == "y":
        md2_hashing()
    elif option == "n":
        menu.hashing_menu()
    else:
        option = input("Do you want to hashing another text? [y/n]: ")


# MD4 Hashing
def md4_hashing():
    print("============ MD4 ============")

    text = input("Enter the text to hashing: ")
    text_encode = text.encode("utf-8")
    print("Hashing.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    hash_object = MD4.new()
    hash_object.update(text_encode)
    hashed_text = hash_object.hexdigest()

    print(f"\nMD4 =>> " + fade.greenblue(f" {hashed_text}"))

    print("")
    option = get_user_option()
    print("")

    if option == "y":
        md4_hashing()
    elif option == "n":
        menu.hashing_menu()
    else:
        option = input("Do you want to hashing another text? [y/n]: ")


# MD5 Hashing
def md5_hashing():
    print("============ MD5 ============")

    text = input("Enter the text to hashing: ")
    text_encode = text.encode("utf-8")
    print("Hashing.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    print("")
    hash_object = hashlib.md5()
    hash_object.update(text_encode)
    hashed_text = hash_object.hexdigest()

    print(f"\nMD5 =>> " + fade.greenblue(f" {hashed_text}"))

    print("")
    option = get_user_option()
    print("")

    if option == "y":
        md5_hashing()
    elif option == "n":
        menu.hashing_menu()
    else:
        option = input("Do you want to hashing another text? [y/n]: ")


# SHA-1 Hashing
def sha1_hashing():
    print("============ SHA-1 ============")

    text = input("Enter the text to hashing: ")
    text_encode = text.encode("utf-8")
    print("Hashing.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    print("")
    hash_object = hashlib.sha1()
    hash_object.update(text_encode)
    hashed_text = hash_object.hexdigest()

    print(f"\nSHA-1 =>> " + fade.greenblue(f" {hashed_text}"))

    print("")
    option = get_user_option()
    print("")

    if option == "y":
        sha1_hashing()
    elif option == "n":
        menu.hashing_menu()
    else:
        option = input("Do you want to hashing another text? [y/n]: ")


# SHA-256 Hashing
def sha256_hashing():
    print("============ SHA-256 ============")

    text = input("Enter the text to hashing: ")
    text_encode = text.encode("utf-8")
    print("Hashing.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    print("")
    hash_object = hashlib.sha256()
    hash_object.update(text_encode)
    hashed_text = hash_object.hexdigest()

    print(f"\nSHA-256 =>> " + fade.greenblue(f" {hashed_text}"))

    print("")
    option = get_user_option()
    print("")

    if option == "y":
        sha256_hashing()
    elif option == "n":
        menu.hashing_menu()
    else:
        option = input("Do you want to hashing another text? [y/n]: ")


# SHA-512 Hashing
def sha512_hashing():
    print("============ SHA-512 ============")

    text = input("Enter the text to hashing: ")
    text_encode = text.encode("utf-8")
    print("Hashing.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    print("")
    hash_object = hashlib.sha512()
    hash_object.update(text_encode)
    hashed_text = hash_object.hexdigest()

    print(f"\nSHA-512 =>> " + fade.greenblue(f" {hashed_text}"))

    print("")
    option = get_user_option()
    print("")

    if option == "y":
        sha512_hashing()
    elif option == "n":
        menu.hashing_menu()
    else:
        option = input("Do you want to hashing another text? [y/n]: ")


# Bcrypt Hashing
def bcrypt_hashing():
    print("============ BCRYPT ============")

    text = input("Enter the text to hashing: ")
    text_encode = text.encode("utf-8")
    salt = int(input("Enter the salt (an integer): "))
    salt = bcrypt.gensalt(salt)
    print("Hashing.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    hashed_text = bcrypt.hashpw(text_encode, salt)
    print(f"\nBcrypt =>> " + fade.greenblue(f" {hashed_text}"))

    option = get_user_option()
    print("")

    if option == "y":
        bcrypt_hashing()
    elif option == "n":
        menu.hashing_menu()
    else:
        option = input("Do you want to hashing another text? [y/n]: ")
