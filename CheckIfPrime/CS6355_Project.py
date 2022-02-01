#Miller-Rabin primality test

print("\n")
num = int(input("Enter a number: "))
print("\n")

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print("0")
           print("\n")
           break
   else:
       print("1")
       print("\n")

# if input number is less than or equal to 1, it is not prime
else:
   print("0")
   print("\n")