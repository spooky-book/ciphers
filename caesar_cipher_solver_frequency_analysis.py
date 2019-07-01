#caesar cipher solver frequency analysis (coincidence index)

import re

def calculate_coincidence_index(string):
	new_string = re.sub("[^a-z]+", "", string)
	
	letter_count = []

	for letter in range(ord("a"), ord("z") + 1):
		letter_count.append(new_string.count(chr(letter)))

	print(letter_count)

	normalising_coefficient = 26	#specific for language

	new_string_len = len(new_string)

	coincidence_index = 0

	for i in range(26):
		coincidence_index += (letter_count[i]/new_string_len) * ((letter_count[i] - 1)/(new_string_len - 1))
	
	return coincidence_index * normalising_coefficient

def main():
	# grabs input and converts it to lowercase
	ciphertext = input("Enter the message: ")
	ciphertext = ciphertext.lower()

	# list of all the possible shift values
	all_shifts = []

	# creates all possible messages and adds it to list
	for shift in range(26):
		plaintext = ''
		for letter in ciphertext:
			if letter.isalpha():
				new_letter = ord(letter) + shift
				if new_letter > ord('z'):
					new_letter -= 26

				plaintext += chr(new_letter)
			else:
				plaintext += letter

		all_shifts.append(plaintext)

	coincidence_index_dict = {}

	for i in range(26):
		coincidence_index_dict[all_shifts[i]] = calculate_coincidence_index(all_shifts[i])
	
	print(coincidence_index_dict)

	
if __name__ == "__main__":
	main()