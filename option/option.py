def get_user_option():
    while True:
        option = input("Do you want to input another password? [y/n]: ")
        if option in ("y", "n"):
            return option
        else:
            print("")
            print("Invalid option!")
            print("")
