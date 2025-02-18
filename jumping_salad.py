print("Welcome to the Jumping Salad Calculator!")

print("How high did the shrimp jump? (in inches)")

shrimp_jump = float(input())

if shrimp_jump > 12:
    print("The shrimp jumped too high!")
elif shrimp_jump < 7:
    print("The shrimp jumped too low!")
else:
    print("The shrimp jumped the perfect height!")