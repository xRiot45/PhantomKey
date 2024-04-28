import time
import fade
import bcrypt
import random
import hashlib
from wordlists import readwordlists
from bruteforce import menu
from option.option import get_user_option
from Crypto.Hash import MD2, MD4, MD5


# MD2 Bruteforce
def md2_bruteforce():
    print("============ MD2 ============")

    text = input("Input the text for brute force: ").strip()
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
        md2_bruteforce()
    elif option == "n":
        menu.bruteforce_menu()
    else:
        option = get_user_option()


# MD4 Bruteforce
def md4_bruteforce():
    print("============ MD4 ============")

    text = input("Input the text for brute force: ").strip()
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
        md4_bruteforce()
    elif option == "n":
        menu.bruteforce_menu()
    else:
        option = get_user_option()


# MD5 Bruteforce
def md5_bruteforce():
    print("============ MD5 ============")

    text = input("Input the text for brute force: ").strip()
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
        md5_bruteforce()
    elif option == "n":
        menu.bruteforce_menu()
    else:
        option = get_user_option()


# SHA-1 Bruteforce
def sha1_brueforce():
    print("============ SHA-1 ============")

    text = input("Input the text for brute force: ").strip()
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
        sha1_brueforce()
    elif option == "n":
        menu.bruteforce_menu()
    else:
        option = get_user_option()


# SHA-256 Bruteforce
def sha256_bruteforce():
    print("============ SHA-256 ============")

    text = input("Input the text for brute force: ").strip()
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
        sha256_bruteforce()
    elif option == "n":
        menu.bruteforce_menu()
    else:
        option = get_user_option()


# SHA-512 Bruteforce
def sha512_bruteforce():
    print("============ SHA-512 ============")

    text = input("Input the text for brute force: ").strip()
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
        sha512_bruteforce()
    elif option == "n":
        menu.bruteforce_menu()
    else:
        option = get_user_option()


# Bcrypt Bruteforce
def bcrypt_bruteforce():
    print("============ BCRYPT ============")

    text = input("Input the text for brute force: ").strip()
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
        bcrypt_bruteforce()
    elif option == "n":
        menu.bruteforce_menu()
    else:
        option = get_user_option()
