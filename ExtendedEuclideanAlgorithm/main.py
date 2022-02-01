def eGCD(a, b):

    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = eGCD(b % a, a)

    x = y1 - (b //a ) * x1
    y = x1

    return gcd, x, y

if __name__ == '__main__':

    print("\n")
    num1 = int(input("Enter the first num (smaller): "))
    num2 = int(input("Enter the second num (bigger): "))
    
    print("\nThe GCD, coeff for smaller num (" + str(num1) + "), and coeff for bigger num (" + str(num2) + ") are: " + str(eGCD(num1, num2)))
    print("\n")