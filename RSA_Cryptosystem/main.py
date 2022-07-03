## Py code implementing the RSA encryption and decryption

## Conda environment "env_sympy"
## "env_sympy" contains gmpy2 as well

import random
from random import randint
import gmpy2
from gmpy2 import mpz
import math
from math import gcd
import sympy
from sympy import isprime

## Select two prime numbers p and q where p != q
p = int(input("\nEnter prime number = "))
q = int(input("\nEnter prime number = "))

if not (isprime(p) & isprime(q)):
    print("\nEither one or both numbers entered are not prime. Enter again.")
    p = int(input("\nEnter prime number = "))
    q = int(input("\nEnter prime number = "))
    
print("\nFirst prime P = ", p)
print("\nSecond prime Q = ", q)

n = mpz(p) * mpz(q)
print("\nP * Q = ", n)

phi = ((mpz(p) - 1) * (mpz(q) - 1))
print("\n(P - 1) * (Q - 1) = ", phi)

## Select e such that it is relatively prime (coprime) to phi and 2 <= e <= phi
e = int(input("\nEnter e = "))
print("\ne = ", e)

if(gcd(mpz(e), mpz(phi)) != 1):
    print("\nThe GCD of", e, "and", phi, "should be 1 for this algorithm to work. Enter e again.")
    e = int(input("\nEnter e = "))

d = pow(mpz(e), -1, mpz(phi))
print("\n(1/e) mod phi = ", d)

print("\nPrivate key = (", d, ",", p, ",", q, ")")

print("\nPublic key = (", e, ",", n, ")")

## Plaintext
## m = randint(1, 1000)
##print("\nRandom plaintext is = ", m)
m = int(input("\nEnter the plaintext to encrypt = "))

## Encryption
c = pow(mpz(m), mpz(e), mpz(n))
print("\nCiphertext = ", c)

## Decryption
p = pow(mpz(c), mpz(d), mpz(n))
print("\nCiphertext after decryption = ", p)

## Check if m and p are equal
if (mpz(m) == mpz(p)):
    print("\n**********Algorithm works**********\n")
else:
    print("\n**********Algorithm does not work**********\n")

## The code does not work for values of m > 5 digits.

## The code also does not work for some values of either e, d, or m.

## While calculating d, for certain values of e, "ValueError: pow() base not invertible" is thrown.