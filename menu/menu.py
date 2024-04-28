import fade
from hashing import menu as encrypt
from bruteforce import menu as bruteforce
from checktype import checktype


def main_menu():
    print("Welcome to PhantomKey, the hashing and brute force tool.")
    print("Version      : 1.0")
    print("Developed by : xRiot")
    print("")
    print("============ CHOOSE A OPTION ============")
    print("[1] Hashing")
    print("[2] Brute Force")
    print("[3] Check Type Hash")
    print("[e] Exit")

    print("")
    option = input("Enter a option: ")

    if option == "1":
        banner = """

██   ██  █████  ███████ ██   ██ ██ ███    ██  ██████  
██   ██ ██   ██ ██      ██   ██ ██ ████   ██ ██       
███████ ███████ ███████ ███████ ██ ██ ██  ██ ██   ███ 
██   ██ ██   ██      ██ ██   ██ ██ ██  ██ ██ ██    ██ 
██   ██ ██   ██ ███████ ██   ██ ██ ██   ████  ██████                                              

        """
        banner_color = fade.greenblue(banner)
        print(banner_color)
        encrypt.hashing_menu()
    elif option == "2":
        banner = """

██████  ██████  ██    ██ ████████ ███████     ███████  ██████  ██████   ██████ ███████ 
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██████  ██    ██    ██    █████       █████   ██    ██ ██████  ██      █████   
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██   ██  ██████     ██    ███████     ██       ██████  ██   ██  ██████ ███████ 

        """
        banner_color = fade.pinkred(banner)
        print(banner_color)
        bruteforce.bruteforce_menu()
    elif option == "3":
        banner = """

 ██████ ██   ██ ███████  ██████ ██   ██     ████████ ██    ██ ██████  ███████
██      ██   ██ ██      ██      ██  ██         ██     ██  ██  ██   ██ ██         
██      ███████ █████   ██      █████          ██      ████   ██████  █████      
██      ██   ██ ██      ██      ██  ██         ██       ██    ██      ██        
 ██████ ██   ██ ███████  ██████ ██   ██        ██       ██    ██      ███████     

        """
        banner_color = fade.purplepink(banner)
        print(banner_color)
        checktype.checktype_hash()
    elif option == "e":
        print("Goodbye!")
    else:
        print("Invalid option!")
        main_menu()
