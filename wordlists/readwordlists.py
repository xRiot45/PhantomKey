def read_wordlist(file_path):
    with open(file_path, "r") as file:
        wordlist = [line.strip() for line in file]
    return wordlist
