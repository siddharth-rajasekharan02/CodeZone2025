def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
opposite = int(input())
hypotenuse = int(input())
common_divisor = gcd(opposite, hypotenuse)
numerator = opposite // common_divisor
denominator = hypotenuse // common_divisor
print(f"{numerator}/{denominator}")
