##### KEY GENERATION #####

p = 7
q = 11
n = (p * q)
g = (n + 1)
l = (p - 1) * (q - 1)

# Public key = (g, n)
print("\nPublic key = (", g, ",", n, ")\n")
# Private key = (p, q, l)
print("Private key = (", p, ",", q, ",", l, ")\n")

##### ENCRYPTION #####

m1 = 25
r = 4
nsquare = (n ** 2)

print("Before encryption, plaintext = ", m1, "\n")

c = int(((g ** m1) * (r ** n)) % nsquare)
print("After encryption, ciphertext = ", c, "\n")

##### DECRYPTION #####

x = int((c ** l) % nsquare)
# print(x)
y = int(pow(l, -1, n))
# print(y)
z = int((x - 1) / 77)
# print(z)

m2 = int((z * y) % n)
print("After decryption, plaintext = ", m2, "\n")