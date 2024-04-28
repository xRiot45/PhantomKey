import time
import fade
import random
from wordlists import readwordlists
from bruteforce import menu
from option.option import get_user_option
from Crypto.Hash import MD2, MD4, MD5


# MD2 Bruteforce
def md2_bruteforce():
    print("============ MD2 ============")

    text = input("Enter the text to brute force: ").strip()
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
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]{};:'\",.<>/?",
                k=len(text),
            )
        )
        print(f"\rAttack: {random_text}", end="", flush=True)
    if not found:
        print(fade.pinkred("\nAttack failed!"))

    option = get_user_option()
    print("")

    if option == "y":
        md2_bruteforce()
    elif option == "n":
        menu.bruteforce_menu()
    else:
        option = input("Do you want to brute force another text? [y/n]: ")


# MD4 Bruteforce
def md4_bruteforce():
    print("============ MD4 ============")

    text = input("Enter the text to brute force: ").strip()
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
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]{};:'\",.<>/?",
                k=len(text),
            )
        )
        print(f"\rAttack: {random_text}", end="", flush=True)
    if not found:
        print(fade.pinkred("\nAttack failed!"))

    option = get_user_option()
    print("")

    if option == "y":
        md4_bruteforce()
    elif option == "n":
        menu.bruteforce_menu()
    else:
        option = input("Do you want to brute force another text? [y/n]: ")


# MD5 Bruteforce
def md5_bruteforce():
    print("============ MD5 ============")

    text = input("Enter the text to brute force: ").strip()
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
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]{};:'\",.<>/?",
                k=len(text),
            )
        )

        print(f"\rAttack: {random_text}", end="", flush=True)
    if not found:
        print(fade.pinkred("\nAttack failed!"))

    option = get_user_option()
    print("")

    if option == "y":
        md5_bruteforce()
    elif option == "n":
        menu.bruteforce_menu()
    else:
        option = input("Do you want to brute force another text? [y/n]: ")
