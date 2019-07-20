import re

def calculate_coincidence_index(string):
	new_string = re.sub("[^a-z]+", "", string)
	
	letter_count = []

	for letter in range(ord("a"), ord("z") + 1):
		letter_count.append(new_string.count(chr(letter)))

	print(letter_count)


	new_string_len = len(new_string)

	coincidence_index = 0

	for i in range(26):
		coincidence_index += letter_count[i] * (letter_count[i] - 1)

	print("Coincidence Index: ", coincidence_index / (new_string_len * (new_string_len - 1)))

	return coincidence_index / (new_string_len * (new_string_len - 1))

def calculate_keylength(string):
	new_string = re.sub("[^a-z]+", "", string)
	I = calculate_coincidence_index(string)

	new_string_len = len(new_string)
	
	k = (0.0265 * new_string_len) / ((0.065 - I) + new_string_len * (I - 0.0385))

	return k