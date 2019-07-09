#substitution cipher

#getting message input and converting to lowercase
plaintext = input("Enter the message: ")
plaintext = plaintext.lower()

#get the new alphabet for the substitution cipher
print("\nNew alphabet should only have 26 letters should not have repeated letters")
key = input("Enter new alphabet: ")
key = key.strip()

if len(key) != 26:
	print("\nMake sure your key has 26 letters, your one has", len(key), "letters")
	exit()

if key.isalpha() == False:
	print("\nMake sure your key only contains letters")
	exit()

ciphertext = ""

#the encryption 
for letter in plaintext:
	if letter.isalpha():
		ciphertext += key[ord(letter) - ord('a')]
	else:
		ciphertext += letter

print("Your message:", ciphertext)

#sample alphabet
#qwertyuiopasdfghjklzxcvbnm