# Py code implementing the ElGamal encryption and decryption

import gmpy2
from gmpy2 import mpz
import random
from random import randint

def main():
    # Large prime
    p = 5809605995369958062791915965639201402176612226902900533702900882779736177890990861472094774477339581147373410185646378328043729800750470098210924487866935059164371588168047540943981644516632755067501626434556398193186628990071248660819361205119793693985433297036118232914410171876807536457391277857011849897410207519105333355801121109356897459426271845471397952675959440793493071628394122780510124618488232602464649876850458861245784240929258426287699705312584509625419513463605155428017165714465363094021609290561084025893662561222573202082865797821865270991145082200656978177192827024538990239969175546190770645685893438011714430426409338676314743571154537142031573004276428701433036381801705308659830751190352946025482059931306571004727362479688415574702596946457770284148435989129632853918392117997472632693078113129886487399347796982772784615865232621289656944284216824611318709764535152507354116344703769998514148343807

    # Generator
    g = 2

    # Random number
    x = randint(1, (mpz(p) - 1))

    y = pow(g, mpz(x), mpz(p))
    # print(mpz(y))

    # Public key pk = (y, g, p)
    # Private key sk = (x)

    # Random plaintext
    m1 = randint(1, 20000)
    # print(m)

    # Random number
    r = randint(1, 20000)
    # print(r)

    # Ciphertext
    c1 = pow(g, r, mpz(p))
    # print(c1)
    c2 = pow((m1 * pow(mpz(y), r)), 1, mpz(p))
    # print(c2)

    # Plaintext
    t = pow(mpz(c1), mpz(-x), mpz(p))
    # print(t)
    m2 = pow((mpz(c2) * mpz(t)), 1, mpz(p))
    # print(m2)

    print("\nKEY GENERATION:")
    print("\nThe first prime is p = ", mpz(p))
    print("\nThe value of g = ", g)
    print("\nThe secret key x = ", mpz(x))
    print("\nThe public key y = ", mpz(y))

    print("\nENCRYPTION:")
    print("\nPlaintext (randomly generated) to be encrypted is m = ", m1)
    print("\nCiphertext is c = (c1, c2) = (", c1, ",", c2, ")")

    print("\nDECRYPTION:")
    print("\nCiphertext to be decrypted is c = (", c1, ",", c2, ")")
    print("\nDecrypted plaintext is m = ", m2, "\n")

if __name__ == "__main__":
    main()