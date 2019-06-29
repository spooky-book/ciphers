#caesar cipher

#getting message input and converting to lowercase
plaintext = input("Enter the message: ")
plaintext = plaintext.lower()

#get input and make sure shift is a integer value
try:
	shift = int(input("Enter shift value: "))
	shift %= 26
except ValueError:
	print("Make sure you enter an integer")
	exit(1)

ciphertext = ""

#the encryption 
for letter in plaintext:
	if letter.isalpha():
		new_letter = ord(letter) + shift
		if new_letter > ord('z'):
			new_letter -= 26

		ciphertext += chr(new_letter)
	else:
		ciphertext += letter

print("Your message:", ciphertext)