number = input("")

for n in range(0, int(number)):
    w = input("")
    w = int(w)
    if w % 10 == 0:
        print("Fake")
    elif w % 2 != 0:
        print("Fake")
    else:
        print("True")
    
