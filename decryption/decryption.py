import time
import random
from wordlists import readwordlists
from decryption import menu
from option.option import get_user_option
from Crypto.Hash import MD2, MD4


# MD2 Decryption
def md2_decrypt():
    print("============ MD2 DECRYPTION ============")

    text = input("Enter the text to decrypt: ").strip()
    print("Decrypting.", end="", flush=True)
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
            print(f"{text} =>> {word}")
            found = True
            break

        random_text = "".join(
            random.choices(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]{};:'\",.<>/?",
                k=len(text),
            )
        )
        print(f"\rDecrypting: {random_text}", end="", flush=True)
    if not found:
        print("Decryption failed!")

    print("")
    option = get_user_option()
    print("")

    if option == "y":
        md2_decrypt()
    elif option == "n":
        menu.decrypt_menu()
    else:
        option = input("Do you want to decrypt another text? [y/n]: ")
