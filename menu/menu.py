import fade
from hashing import menu as encrypt
from cracking import menu as cracking
from checktype import checktype


def main_menu():
    print("Welcome to PhantomKey, the hashing and cracking password tool.")
    print("Version      : 1.0")
    print("Developed by : xRiot")
    print("")
    print("============ CHOOSE A OPTION ============")
    print("[1] Hashing")
    print("[2] Cracking")
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


 ██████ ██████   █████   ██████ ██   ██ ██ ███    ██  ██████  
██      ██   ██ ██   ██ ██      ██  ██  ██ ████   ██ ██       
██      ██████  ███████ ██      █████   ██ ██ ██  ██ ██   ███ 
██      ██   ██ ██   ██ ██      ██  ██  ██ ██  ██ ██ ██    ██ 
 ██████ ██   ██ ██   ██  ██████ ██   ██ ██ ██   ████  ██████  
                            

        """
        banner_color = fade.pinkred(banner)
        print(banner_color)
        cracking.cracking_menu()
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
