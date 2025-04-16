from fractions import Fraction 

adjacent = input("Adjacent Side: ")

hypotenuse = input("Hypotenuse: ")

output = int(adjacent) / int(hypotenuse)



f = Fraction(float(output))

print(f)