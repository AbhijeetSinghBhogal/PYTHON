import tkinter as tk
import random
from math import floor
from math import sqrt

root = tk.Tk()
root.title("RSA Encryption/Decryption")
canvas = tk.Canvas(root, width=800, height=600)
canvas.grid(columnspan=3, rowspan=8)

RANDOM_START = 1e3
RANDOM_END = 1e5

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, floor(sqrt(num))):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modular_inverse(a, b):
    if a == 0:
        return b, 0, 1
    div, x1, y1 = modular_inverse(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return div, x, y

def Generate_Large_Prime_P(start=0, end=5000):
    Generate_Large_Prime_P.num = random.randint(start, end)
    while not is_prime(Generate_Large_Prime_P.num):
        Generate_Large_Prime_P.num = random.randint(start, end)

    textBox1 = tk.Text(root, height=1, width=15, padx=5, pady=5, font=('bold', 20))
    textBox1.insert(1.0, Generate_Large_Prime_P.num)
    textBox1.tag_configure('center', justify='center')
    textBox1.tag_add('center', 1.0, "end")
    textBox1.grid(row=0, column=2)

    return Generate_Large_Prime_P.num

def Generate_Large_Prime_Q(start=0, end=5000):
    Generate_Large_Prime_Q.num = random.randint(start, end)
    while not is_prime(Generate_Large_Prime_Q.num):
        Generate_Large_Prime_Q.num = random.randint(start, end)

    textBox2 = tk.Text(root, height=1, width=15, padx=5, pady=5, font=('bold', 20))
    textBox2.insert(1.0, Generate_Large_Prime_Q.num)
    textBox2.tag_configure('center', justify='center')
    textBox2.tag_add('center', 1.0, "end")
    textBox2.grid(row=1, column=2)

    return Generate_Large_Prime_Q.num

def Multiply_P_Q():
    p = Generate_Large_Prime_P.num
    q = Generate_Large_Prime_Q.num
    Multiply_P_Q.n = p * q

    textBox3 = tk.Text(root, height=1, width=15, padx=5, pady=5, font=('bold', 20))
    textBox3.insert(1.0, Multiply_P_Q.n)
    textBox3.tag_configure('center', justify='center')
    textBox3.tag_add('center', 1.0, "end")
    textBox3.grid(row=2, column=2)

    return Multiply_P_Q.n

def Public_Key_E():
    p = Generate_Large_Prime_P.num
    q = Generate_Large_Prime_Q.num
    Public_Key_E.phi = (p-1)*(q-1)
    Public_Key_E.e = random.randrange(1, Public_Key_E.phi)
 
    textBox4 = tk.Text(root, height=1, width=15, padx=5, pady=5, font=('bold', 20))
    textBox4.insert(1.0, Public_Key_E.e)
    textBox4.tag_configure('center', justify='center')
    textBox4.tag_add('center', 1.0, "end")
    textBox4.grid(row=3, column=2)

    return Public_Key_E.e

def Private_Key_D():
    while gcd(Public_Key_E.e, Public_Key_E.phi) != 1:
        Public_Key_E.e = random.randrange(1, Public_Key_E.phi)
    Private_Key_D.d = modular_inverse(Public_Key_E.e, Public_Key_E.phi)[1]

    textBox5 = tk.Text(root, height=1, width=15, padx=5, pady=5, font=('bold', 20))
    textBox5.insert(1.0, Private_Key_D.d)
    textBox5.tag_configure('center', justify='center')
    textBox5.tag_add('center', 1.0, "end")
    textBox5.grid(row=4, column=2)

    return (Private_Key_D.d, Multiply_P_Q.n), (Public_Key_E.e, Multiply_P_Q.n)

def Message():

    Message.message = input1.get()

    textBox6 = tk.Text(root, height=1, width=60, padx=5, pady=5, font=('bold', 20))
    textBox6.insert(1.0, Message.message)
    textBox6.tag_configure('center', justify='center')
    textBox6.tag_add('center', 1.0, "end")
    textBox6.grid(row=6, column=2)
    
    return Message.message

def Encrypt_Message():

    public_key = Public_Key_E.e, Multiply_P_Q.n

    Encrypt_Message.cipher_text = []

    for char in Message.message:
        a = ord(char)
        Encrypt_Message.cipher_text.append(pow(a, Public_Key_E.e, Multiply_P_Q.n))

    textBox7 = tk.Text(root, height=1, width=60, padx=5, pady=5, font=('bold', 20))
    textBox7.insert(1.0, Encrypt_Message.cipher_text)
    textBox7.tag_configure('center', justify='center')
    textBox7.tag_add('center', 1.0, "end")
    textBox7.grid(row=6, column=2)

    return Encrypt_Message.cipher_text

def Decrypt_Message():

    private_key = Private_Key_D.d, Multiply_P_Q.n

    plain_text = ''

    for num in Encrypt_Message.cipher_text:
        a = pow(num, Private_Key_D.d, Multiply_P_Q.n)
        plain_text = plain_text + str(chr(a))

    textBox8 = tk.Text(root, height=1, width=60, padx=5, pady=5, font=('bold', 20))
    textBox8.insert(1.0, plain_text)
    textBox8.tag_configure('center', justify='center')
    textBox8.tag_add('center', 1.0, "end")
    textBox8.grid(row=7, column=2)

    return plain_text

label1 = tk.Label(root, text="1. Prime p", font=('bold', 20)).grid(row=0, column=0)
button1 = tk.Button(root, text="Generate", command=lambda: Generate_Large_Prime_P(), font=('bold', 18)).grid(row=0, column=1)

label2 = tk.Label(root, text="2. Prime q", font=('bold', 20)).grid(row=1, column=0)
button2 = tk.Button(root, text="Generate", command=lambda: Generate_Large_Prime_Q(), font=('bold', 18)).grid(row=1, column=1)

label3 = tk.Label(root, text="3. n = p * q", font=('bold', 20)).grid(row=2, column=0)
button3 = tk.Button(root, text="Compute", command=lambda: Multiply_P_Q(), font=('bold', 18)).grid(row=2, column=1)

label4 = tk.Label(root, text="4. Public key e", font=('bold', 20)).grid(row=3, column=0)
button4 = tk.Button(root, text="Generate", command=lambda: Public_Key_E(), font=('bold', 18)).grid(row=3, column=1)

label5 = tk.Label(root, text="5. Private key d", font=('bold', 20)).grid(row=4, column=0)
button5 = tk.Button(root, text="Calculate", command=lambda: Private_Key_D(), font=('bold', 18)).grid(row=4, column=1)

label6 = tk.Label(root, text="6. Message m", font=('bold', 20)).grid(row=5, column=0)
input1 = tk.Entry(root, width=25, font=('bold', 20))
input1.insert(0, "")
input1.grid(row=5, column=1)
button6 = tk.Button(root, text="Submit", command=lambda: Message(), font=('bold', 18)).grid(row=5, column=2)

label7 = tk.Label(root, text="7. Encrypt c = m^e mod n", font=('bold', 20)).grid(row=6, column=0)
button7 = tk.Button(root, text="Encrypt", command=lambda: Encrypt_Message(), font=('bold', 18)).grid(row=6, column=1)

label8 = tk.Label(root, text="8. Decrypt m = c^d mod n", font=('bold', 20)).grid(row=7, column=0)
button8 = tk.Button(root, text="Decrypt", command=lambda: Decrypt_Message(), font=('bold', 18)).grid(row=7, column=1)

root.mainloop()