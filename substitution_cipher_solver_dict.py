#substitution cipher
from make_word_patterns import *
import fnmatch
import re

def main():
	#getting message input and converting to lowercase
	ciphertext = input("Enter the message: ")
	ciphertext = ciphertext.lower()
	ciphertext_only_letters = re.sub("[^a-zA-Z' ]+", "", ciphertext)

	ciphertext_only_letters_split = ciphertext_only_letters.split()

	ciphertext_word_pattern = []
	for word in ciphertext_only_letters_split:
		ciphertext_word_pattern.append(create_word_pattern(word))

	all_word_pattern = grab_create_all_word_pattern()

	print(ciphertext_word_pattern)

	only_matching_patterns = {}

	for pattern in ciphertext_word_pattern:
		if pattern in all_word_pattern:
			#print(pattern + ":", all_word_pattern[pattern])
			only_matching_patterns[pattern] = all_word_pattern[pattern]
		else:
			#print(pattern + ":", "No matching word patterns")
			only_matching_patterns[pattern] = []

	sorted_ciphertext_word_pattern = sorted(ciphertext_word_pattern, key=len, reverse=True)
	print(sorted_ciphertext_word_pattern)
	print(only_matching_patterns)

	key = list("??????????????????????????")

def substitution(text, key):
	text = text.strip()
	new_text = ""
	for letter in text:
		if letter.isalpha():
			new_text += key[ord(letter) - ord('a')]
		else:
			new_text += letter

	return new_text

if __name__ == "__main__":
	main()