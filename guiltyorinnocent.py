string=input("")
string1 = (string[0].lower()).strip()
if string1 in "abcdefghijklm":
    print(f"{string} is guilty")
elif string1 in "nopqrstuzwxyz":
    print(f"{string} is not guilty")
