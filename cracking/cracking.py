import time
import fade
import bcrypt
import random
import hashlib
from wordlists import readwordlists
from cracking import menu
from option.option import get_user_option
from Crypto.Hash import MD2, MD4, MD5


# MD2 Cracking
def md2_cracking():
    print("============ MD2 ============")

    text = input("Input the text for cracking: ").strip()
    print("Attack.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    wordlist_path = "wordlists/wordlists.txt"
    wordlist = readwordlists.read_wordlist(wordlist_path)

    random.shuffle(wordlist)

    found = False
    for word in wordlist:
        hash_object = MD2.new()
        hash_object.update(word.encode("utf-8"))
        hashed_text = hash_object.hexdigest()

        if hashed_text == text:
            print("")
            print(f"{text} =>>" + fade.greenblue(f" {word}"))
            found = True
            break

        random_text = "".join(
            random.choices(
                "(abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]{};:'\",.<>/?)",
                k=len("abcdefghij"),
            )
        )
        print(f"\rAttack: ({random_text})", end="", flush=True)
    if not found:
        print(fade.pinkred("\nAttack failed!"))

    option = get_user_option()
    print("")

    if option == "y":
        md2_cracking()
    elif option == "n":
        menu.cracking_menu()
    else:
        option = get_user_option()


# MD4 Cracking
def md4_cracking():
    print("============ MD4 ============")

    text = input("Input the text for cracking: ").strip()
    print("Attack.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    wordlist_path = "wordlists/wordlists.txt"
    wordlist = readwordlists.read_wordlist(wordlist_path)

    random.shuffle(wordlist)

    found = False
    for word in wordlist:
        hash_object = MD4.new()
        hash_object.update(word.encode("utf-8"))
        hashed_text = hash_object.hexdigest()

        if hashed_text == text:
            print("")
            print(f"{text} =>>" + fade.greenblue(f" {word}"))
            found = True
            break

        random_text = "".join(
            random.choices(
                "(abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]{};:'\",.<>/?)",
                k=len("abcdefghij"),
            )
        )
        print(f"\rAttack: ({random_text})", end="", flush=True)
    if not found:
        print(fade.pinkred("\nAttack failed!"))

    option = get_user_option()
    print("")

    if option == "y":
        md4_cracking()
    elif option == "n":
        menu.cracking_menu()
    else:
        option = get_user_option()


# MD5 Cracking
def md5_cracking():
    print("============ MD5 ============")

    text = input("Input the text for cracking: ").strip()
    print("Attack.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    worlist_path = "wordlists/wordlists.txt"
    wordlist = readwordlists.read_wordlist(worlist_path)

    random.shuffle(wordlist)

    found = False
    for word in wordlist:
        hash_object = MD5.new()
        hash_object.update(word.encode("utf-8"))
        hashed_text = hash_object.hexdigest()

        if hashed_text == text:
            print("")
            print(f"{text} =>> " + fade.greenblue(f"{word}"))
            found = True
            break

        random_text = "".join(
            random.choices(
                "(abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]{};:'\",.<>/?)",
                k=len("abcdefghij"),
            )
        )

        print(f"\rAttack: ({random_text})", end="", flush=True)
    if not found:
        print(fade.pinkred("\nAttack failed!"))

    option = get_user_option()
    print("")

    if option == "y":
        md5_cracking()
    elif option == "n":
        menu.cracking_menu()
    else:
        option = get_user_option()


# SHA-1 Cracking
def sha1_cracking():
    print("============ SHA-1 ============")

    text = input("Input the text for cracking: ").strip()
    print("Attack.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    wordlist_path = "wordlists/wordlists.txt"
    wordlist = readwordlists.read_wordlist(wordlist_path)

    random.shuffle(wordlist)

    found = False
    for word in wordlist:
        hash_object = hashlib.sha1()
        hash_object.update(word.encode("utf-8"))
        hashed_text = hash_object.hexdigest()

        if hashed_text == text:
            print("")
            print(f"{text} =>> " + fade.greenblue(f"{word}"))
            found = True
            break

        random_text = "".join(
            random.choices(
                "(abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]{};:'\",.<>/?)",
                k=len("abcdefghij"),
            )
        )

        print(f"\rAttack: ({random_text})", end="", flush=True)
    if not found:
        print(fade.pinkred("\nAttack failed!"))

    option = get_user_option()
    print("")

    if option == "y":
        sha1_cracking()
    elif option == "n":
        menu.cracking_menu()
    else:
        option = get_user_option()


# SHA-256 Cracking
def sha256_cracking():
    print("============ SHA-256 ============")

    text = input("Input the text for cracking: ").strip()
    print("Attack.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    wordlist_path = "wordlists/wordlists.txt"
    wordlist = readwordlists.read_wordlist(wordlist_path)

    random.shuffle(wordlist)

    found = False
    for word in wordlist:
        hash_object = hashlib.sha256()
        hash_object.update(word.encode("utf-8"))
        hashed_text = hash_object.hexdigest()

        if hashed_text == text:
            print("")
            print(f"{text} =>> " + fade.greenblue(f"{word}"))
            found = True
            break

        random_text = "".join(
            random.choices(
                "(abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]{};:'\",.<>/?)",
                k=len("abcdefghij"),
            )
        )

        print(f"\rAttack: ({random_text})", end="", flush=True)
    if not found:
        print(fade.pinkred("\nAttack failed!"))

    option = get_user_option()
    print("")

    if option == "y":
        sha256_cracking()
    elif option == "n":
       menu.cracking_menu()
    else:
        option = get_user_option()


# SHA-512 Cracking
def sha512_cracking():
    print("============ SHA-512 ============")

    text = input("Input the text for cracking: ").strip()
    print("Attack.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    wordlist_path = "wordlists/wordlists.txt"
    wordlist = readwordlists.read_wordlist(wordlist_path)

    random.shuffle(wordlist)

    found = False
    for word in wordlist:
        hash_object = hashlib.sha512()
        hash_object.update(word.encode("utf-8"))
        hashed_text = hash_object.hexdigest()

        if hashed_text == text:
            print("")
            print(f"{text} =>> " + fade.greenblue(f"{word}"))
            found = True
            break

        random_text = "".join(
            random.choices(
                "(abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]{};:'\",.<>/?)",
                k=len("abcdefghij"),
            )
        )

        print(f"\rAttack: ({random_text})", end="", flush=True)
    if not found:
        print(fade.pinkred("\nAttack failed!"))

    option = get_user_option()
    print("")

    if option == "y":
        sha512_cracking()
    elif option == "n":
        menu.cracking_menu()
    else:
        option = get_user_option()


# Bcrypt Cracking
def bcrypt_cracking():
    print("============ BCRYPT ============")

    text = input("Input the text for cracking: ").strip()
    print("Attack.", end="", flush=True)
    for i in range(5):
        time.sleep(1)
        print(".", end="", flush=True)

    wordlist_path = "wordlists/wordlists.txt"
    wordlist = readwordlists.read_wordlist(wordlist_path)

    random.shuffle(wordlist)
    salt = bcrypt.gensalt()

    found = False
    for word in wordlist:
        hashed_text = bcrypt.hashpw(word.encode("utf-8"), salt).decode("utf-8")

        if hashed_text == text:
            print("")
            print(f"{text} =>> " + fade.greenblue(f"{word}"))
            found = True
            break

        random_text = "".join(
            random.choices(
                "(abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]{};:'\",.<>/?)",
                k=len("abcdefghij"),
            )
        )

        print(f"\rAttack: ({random_text})", end="", flush=True)
    if not found:
        print(fade.pinkred("\nAttack failed!"))

    option = get_user_option()
    print("")

    if option == "y":
        bcrypt_cracking()
    elif option == "n":
        menu.cracking_menu()
    else:
        option = get_user_option()
