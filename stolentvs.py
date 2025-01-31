import math

print("""A thief has stolen many TVs from an electronic store. The cameras didn't manage to
	  catch their face, so the relevant insurance is providing replacements for the lost product.
	  We need you to make us a program to determine how many TVs to replace for a given 
	  amount of loss. The first, and only, line of input is the value of TVs stolen. Each TV is worth 89 dollars.
Determine and print the number of TVs stolen for the respective value, rounded to the
nearest whole.""")

print("Okay, everything after this line is part of the solution code.")

# Solution code

value_of_stolen_tvs = int(input("What is the value of the stolen TVs? "))\

number_of_tvs = math.ceil(value_of_stolen_tvs / 89)

print(f"The number of TVs stolen is {number_of_tvs}.")