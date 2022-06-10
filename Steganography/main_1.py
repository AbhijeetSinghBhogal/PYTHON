# Python code to perform steganography using the Stegano module.

import stegano
from stegano import lsb

filePath = "/Users/abhijeetsingh/PYTHON/Steganography/Warm_Poly.png"

secretMessage = input("\nEnter the secret message to embed in the image: ")

secretImage = lsb.hide(filePath, secretMessage)

print("\nSecret message has been embedded in: ", filePath)

secretImage.save("/Users/abhijeetsingh/PYTHON/Steganography/Warm_Poly_New.png")

choice = input("\nDo you want to display the embedded message? (y/n): ")

if(choice == "y"):
    print("\nSecret message embedded in the image is: ", lsb.reveal("/Users/abhijeetsingh/PYTHON/Steganography/Warm_Poly_New.png"))
else:
    print("\nSecret message cannot be displayed.")

print("\n")