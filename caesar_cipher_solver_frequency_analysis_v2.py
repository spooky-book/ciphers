#caesar cipher solver frequency analysis (coincidence index)
from ngram_class import nGramInfo
import re

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

	fitness_scores = {}

	print("Enter '1' for monograms")
	print("Enter '2' for bigrams")
	print("Enter '3' for trigrams")
	print("Enter '4' for quadgrams")
	print("Note: quadgrams can only do analysis on messages >= 4 characters\ntrigrams for >= 3 and so on \n(if you need a program to help decipher a < 4 letter caesar cipher RIP)")
	mode = input("Enter Mode: ")
	mode = mode.strip().lower()

	if mode == '1':
		file_name = "english_monograms.txt"
	elif mode == '2':
		file_name = "english_bigrams.txt"
	elif mode == '3':
		file_name = "english_trigrams.txt"
	elif mode == '4':
		file_name = "english_quadgrams.txt"
	else: 
		print("Make sure input is correct")
		exit()

	calculator = nGramInfo(file_name)
	
	for i in range(26):
		temp = re.sub("[^a-zA-Z']+", "", all_shifts[i])
		fitness_scores[all_shifts[i]] = [calculator.calculate_fitness_score(temp), i]
	
	sorted_fitness_scores = sorted(((value, key) for (key, value) in fitness_scores.items()), reverse=True)

	print("\nBelow are the 26 shifts of the cipher ordered by most likely the message\n")

	print(" Message | Score | Shift")
	for i in range(26):
		print(">{} | {:<4.15f} | {}".format(sorted_fitness_scores[i][1], sorted_fitness_scores[i][0][0], sorted_fitness_scores[i][0][1]))

	
if __name__ == "__main__":
	main()