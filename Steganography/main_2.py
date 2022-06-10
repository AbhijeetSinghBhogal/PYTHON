# Python code to perform steganography using the Stegano module.

import stegano
from stegano import lsbset
from stegano.lsbset import generators

filePath = "/Users/abhijeetsingh/PYTHON/Steganography/Warm_Poly.png"

secretMessage = input("\nEnter the secret message to embed in the image: ")

secretImage = lsbset.hide(filePath, secretMessage, generators.eratosthenes())

print("\nSecret message has been embedded in a steged copy of: ", filePath)

secretImage.save("/Users/abhijeetsingh/PYTHON/Steganography/Warm_Poly_Steged.png")

choice = input("\nDo you want to display the embedded message? (y/n): ")

if(choice == "y"):
    print("\nSecret message embedded in the image is: ", lsbset.reveal("/Users/abhijeetsingh/PYTHON/Steganography/Warm_Poly_Steged.png", generators.eratosthenes()))
else:
    print("\nSecret message cannot be displayed.")

print("\n")