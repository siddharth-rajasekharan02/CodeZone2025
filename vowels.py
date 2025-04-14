string = input("")
x=0
for character in string:
    if character != "a" or "e" or "i" or "o" or "u" or "A" or "E" or "I" or "O" or "U":
        x = x+1
    
print(str(x-1))
