import random

lowercaseAlphabet = "abcdefghijklmnopqrstuvwxyz"
uppercaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "~`!@#$%^&*()_-+=[]|;:<>,./?"

all = lowercaseAlphabet + uppercaseAlphabet + numbers + symbols

length = int(input("\nHow long do you want the password? = "))

password = "".join(random.sample(all, length))

print("\nHere is your new password = ", password, "\n")