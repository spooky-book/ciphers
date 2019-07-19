#vignere cipher
#i guess also kinda one time pad

#getting message input and converting to lowercase
plaintext = input("Enter the message: ")
plaintext = plaintext.lower().strip()

#get the key for the vignere cipher
print("Enter a sequence of letters for key")
key = input("Enter the key: ")
key = key.lower().strip()

# checking if key is all alphabetical
if key.isalpha() == False:
	print("\nMake sure your key only contains letters")
	exit()

# making sure key is at least as long as plaintext
key = key * int((len(plaintext) / len(key)) + 1)

ciphertext = ""

mode = input("Enter 'e' for encryption and 'd' for decryption")
mode = mode.lower().strip()

if len(mode) != 1 or mode.isalpha() == False:
	print("Make sure input is correct")
	exit()

if mode == 'e':
	#the encryption 
	key_iter = 0
	for i in range(len(plaintext)):
		if plaintext[i].isalpha():
			new_letter = ord(plaintext[i]) + ord(key[key_iter]) - ord('a')

			if new_letter > ord("z"):
				new_letter -= 26

			ciphertext += chr(new_letter)
			key_iter += 1
		else:
			ciphertext += plaintext[i]
elif mode == 'd':
	# the decryption
	key_iter = 0
	for i in range(len(plaintext)):
		if plaintext[i].isalpha():
			new_letter = ord(plaintext[i]) - ord(key[key_iter]) + ord('a')

			if new_letter < ord("a"):
				new_letter += 26

			ciphertext += chr(new_letter)
			key_iter += 1
		else:
			ciphertext += plaintext[i]
else:
	print("Make sure only 'e' or 'd' is inputted")
	exit()


print("Your message:", ciphertext)