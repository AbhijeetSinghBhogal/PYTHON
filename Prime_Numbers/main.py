# All prime numbers are greater than 1

lower = 0
upper = 50

print("Prime numbers between", lower, "and", upper, "are:\n")

for num in range(lower, upper+1):
    if num>1:
        for i in range(2, num):
            if (num%i) == 0:
                break
        else:
            print(num)