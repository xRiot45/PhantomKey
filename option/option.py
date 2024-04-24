def get_user_option():
    while True:
        option = input("Do you want to encrypt another text? [y/n]: ")
        if option in ("y", "n"):
            return option
        else:
            print("")
            print("Invalid option!")
            print("")
