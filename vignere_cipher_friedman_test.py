from friedman_test import *

ciphertext = input("Enter the message: ")
ciphertext = ciphertext.lower().strip()

print("calculating approx key length")

keylength = calculate_keylength(ciphertext)

print(keylength)