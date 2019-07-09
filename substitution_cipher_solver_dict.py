#substitution cipher

import re

def main():
	#getting message input and converting to lowercase
	ciphertext = input("Enter the message: ")
	ciphertext = ciphertext.lower()
	ciphertext_only_letters = re.sub("[^a-zA-Z' ]+", "", words_string)
	ciphertext_only_letters_list = ciphertext_only_letters.split()

	ciphertext_pattern = create_word_pattern(ciphertext)
	print(ciphertext_pattern)

#takes in a string and returns a list of word patterns
def create_word_pattern(words_string):
	
	word_pattern_list = []
	
	for word in ciphertext_only_letters_list:
		word_pattern = ""
		i = 0
		seen = {}	#dictionary
		for letter in word:
			if letter in seen:
				word_pattern += seen[letter]
			else:
				seen[letter] = str(i)
				word_pattern += str(i)
				i += 1

		word_pattern_list.append([word_pattern, word])


	return word_pattern_list

if __name__ == "__main__":
	main()