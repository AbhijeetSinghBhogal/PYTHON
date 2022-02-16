#recursive implementation
def gcdRecur(a, b):

    if a % b == 0:
        return b

    return gcdRecur(b, a % b)

#iterative implementation
def gcdIter(a, b):

    while a % b != 0:
        a, b = b, a % b

    return b

if __name__ == '__main__':

    num1 = int(input("Enter the first num: "))
    num2 = int(input("Enter the second num: "))

    print("\nGCD of" , num1 , "and" , num2 , "using recursion is: " , gcdRecur(num1, num2))
    print("\nGCD of " + str(num1) + " and " + str(num2) + " using iteration is: " + str(gcdIter(num1, num2)))