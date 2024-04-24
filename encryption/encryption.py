import time
import bcrypt
import hashlib
from encryption import menu
from option.option import get_user_option
from Crypto.Hash import MD2, MD4


# MD2 Encryption
def md2_encrypt():
    print("============ MD2 ============")

    text = input("Enter the text to encrypt: ").strip()
    text_encode = text.encode("utf-8")
    print("Encrypting.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    hash_object = MD2.new()
    hash_object.update(text_encode)
    hashed_text = hash_object.hexdigest()

    print(f"\nMD2 =>> {hashed_text}")

    print("")
    option = get_user_option()
    print("")

    if option == "y":
        md2_encrypt()
    elif option == "n":
        menu.encrypt_menu()
    else:
        option = input("Do you want to encrypt another text? [y/n]: ")


# MD4 Encryption
def md4_encrypt():
    print("============ MD4 ============")

    text = input("Enter the text to encrypt: ")
    text_encode = text.encode("utf-8")
    print("Encrypting.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    hash_object = MD4.new()
    hash_object.update(text_encode)
    hashed_text = hash_object.hexdigest()

    print(f"\nMD4 =>> {hashed_text}")

    print("")
    option = get_user_option()
    print("")

    if option == "y":
        md4_encrypt()
    elif option == "n":
        menu.encrypt_menu()
    else:
        option = input("Do you want to encrypt another text? [y/n]: ")


# MD5 Encryption
def md5_encrypt():
    print("============ MD5 ============")

    text = input("Enter the text to encrypt: ")
    text_encode = text.encode("utf-8")
    print("Encrypting.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    print("")
    hash_object = hashlib.md5()
    hash_object.update(text_encode)
    hashed_text = hash_object.hexdigest()

    print(f"\nMD5 =>> {hashed_text}")

    print("")
    option = get_user_option()
    print("")

    if option == "y":
        md5_encrypt()
    elif option == "n":
        menu.encrypt_menu()
    else:
        option = input("Do you want to encrypt another text? [y/n]: ")


# SHA-1 Encryption
def sha1_encrypt():
    print("============ SHA-1 ============")

    text = input("Enter the text to encrypt: ")
    text_encode = text.encode("utf-8")
    print("Encrypting.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    print("")
    hash_object = hashlib.sha1()
    hash_object.update(text_encode)
    hashed_text = hash_object.hexdigest()

    print(f"\nSHA-1 =>> {hashed_text}")

    print("")
    option = get_user_option()
    print("")

    if option == "y":
        sha1_encrypt()
    elif option == "n":
        menu.encrypt_menu()
    else:
        option = input("Do you want to encrypt another text? [y/n]: ")


# SHA-256 Encryption
def sha256_encrypt():
    print("============ SHA-256 ============")

    text = input("Enter the text to encrypt: ")
    text_encode = text.encode("utf-8")
    print("Encrypting.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    print("")
    hash_object = hashlib.sha256()
    hash_object.update(text_encode)
    hashed_text = hash_object.hexdigest()

    print(f"\nSHA-256 =>> {hashed_text}")

    print("")
    option = get_user_option()
    print("")

    if option == "y":
        sha256_encrypt()
    elif option == "n":
        menu.encrypt_menu()
    else:
        option = input("Do you want to encrypt another text? [y/n]: ")


# SHA-512 Encryption
def sha512_encrypt():
    print("============ SHA-512 ============")

    text = input("Enter the text to encrypt: ")
    text_encode = text.encode("utf-8")
    print("Encrypting.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    print("")
    hash_object = hashlib.sha512()
    hash_object.update(text_encode)
    hashed_text = hash_object.hexdigest()

    print(f"\nSHA-512 =>> {hashed_text}")

    print("")
    option = get_user_option()
    print("")

    if option == "y":
        sha512_encrypt()
    elif option == "n":
        menu.encrypt_menu()
    else:
        option = input("Do you want to encrypt another text? [y/n]: ")


# Bcrypt Encryption
def bcrypt_encrypt():
    print("============ BCRYPT ============")

    text = input("Enter the text to encrypt: ")
    text_encode = text.encode("utf-8")
    salt = int(input("Enter the salt (an integer): "))
    salt = bcrypt.gensalt(rounds=salt)
    print("Encrypting.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    hashed_text = bcrypt.hashpw(text_encode, salt)
    print(f"\nBcrypt =>> {hashed_text}")

    print("")
    option = get_user_option()
    print("")

    if option == "y":
        bcrypt_encrypt()
    elif option == "n":
        menu.encrypt_menu()
    else:
        option = input("Do you want to encrypt another text? [y/n]: ")
