import tkinter as tk
import random

root = tk.Tk()
root.title("Diffie-Hellman Key Exchange")
canvas = tk.Canvas(root, width=1000, height=600)
canvas.grid(columnspan=3, rowspan=8)

def Random_X():
    Random_X.x = int(input1.get())
    return Random_X.x

def Random_Y():
    Random_Y.y = int(input2.get())
    return Random_Y.y

def Compute_X():

    largePrimeP = 65537
    primaryRootG = 3

    Compute_X.k1 = pow(primaryRootG, Random_X.x, largePrimeP)

    textBox1 = tk.Text(root, height=1, width=20, padx=5, pady=5, font=('bold', 20))
    textBox1.insert(1.0, Compute_X.k1)
    textBox1.tag_configure('center', justify='center')
    textBox1.tag_add('center', 1.0, "end")
    textBox1.grid(row=2, column=2)

    return Compute_X.k1

def Compute_Y():

    largePrimeP = 65537
    primaryRootG = 3

    Compute_Y.k2 = pow(primaryRootG, Random_Y.y, largePrimeP)

    textBox2 = tk.Text(root, height=1, width=20, padx=5, pady=5, font=('bold', 20))
    textBox2.insert(1.0, Compute_Y.k2)
    textBox2.tag_configure('center', justify='center')
    textBox2.tag_add('center', 1.0, "end")
    textBox2.grid(row=4, column=2)

    return Compute_Y.k2

def Session_Key_Y():

    largePrimeP = 65537
    primaryRootG = 3

    sessionKey1 = pow(Compute_Y.k2, Random_X.x, largePrimeP)

    textBox3 = tk.Text(root, height=1, width=20, padx=5, pady=5, font=('bold', 20))
    textBox3.insert(1.0, sessionKey1)
    textBox3.tag_configure('center', justify='center')
    textBox3.tag_add('center', 1.0, "end")
    textBox3.grid(row=6, column=2)

    return sessionKey1

def Session_Key_X():

    largePrimeP = 65537
    primaryRootG = 3

    sessionKey2 = pow(Compute_X.k1, Random_Y.y, largePrimeP)

    textBox4 = tk.Text(root, height=1, width=20, padx=5, pady=5, font=('bold', 20))
    textBox4.insert(1.0, sessionKey2)
    textBox4.tag_configure('center', justify='center')
    textBox4.tag_add('center', 1.0, "end")
    textBox4.grid(row=7, column=2)

    return sessionKey2

label1 = tk.Label(root, text="1. Given a large prime p = 65537, a primary root g = 3", font=('bold', 20)).grid(row=0, column=0)

label2 = tk.Label(root, text="2. Choose a random number x", font=('bold', 20)).grid(row=1, column=0)
input1 = tk.Entry(root, width=10, font=('bold', 20))
input1.insert(0, "")
input1.grid(row=1, column=1)
button1 = tk.Button(root, text="Choose", command=lambda: Random_X(), font=('bold', 18)).grid(row=1, column=2)

label3 = tk.Label(root, text="3. Compute X = g^x mod p", font=('bold', 20)).grid(row=2, column=0)
button2 = tk.Button(root, text="Compute", font=('bold', 18), command=lambda: Compute_X()).grid(row=2, column=1)

label4 = tk.Label(root, text="4. Choose a random number y", font=('bold', 20)).grid(row=3, column=0)
input2 = tk.Entry(root, width=15, font=('bold', 20))
input2.insert(0, "")
input2.grid(row=3, column=1)
button3 = tk.Button(root, text="Choose", command=lambda: Random_Y(), font=('bold', 18)).grid(row=3, column=2)

label5 = tk.Label(root, text="5. Compute Y = g^y mod p", font=('bold', 20)).grid(row=4, column=0)
button4 = tk.Button(root, text="Compute", font=('bold', 18), command=lambda: Compute_Y()).grid(row=4, column=1)

label6 = tk.Label(root, text="6. Calculate the session key K = g^xy mod p", font=('bold', 20)).grid(row=5, column=0)

label7 = tk.Label(root, text="K = Y^x mod p", font=('bold', 20)).grid(row=6, column=0)
button5 = tk.Button(root, text="Calculate", font=('bold', 18), command=lambda: Session_Key_Y()).grid(row=6, column=1)

label8 = tk.Label(root, text="K = X^y mod p", font=('bold', 20)).grid(row=7, column=0)
button6 = tk.Button(root, text="Calculate", font=('bold', 18), command=lambda: Session_Key_X()).grid(row=7, column=1)

root.mainloop()