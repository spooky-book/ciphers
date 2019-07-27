import re, random

from ngram_class import nGramInfo

#substitution cipher

def main():
	# grabs input and makes it lower case
	ciphertext = input("Enter the message: ")
	ciphertext = ciphertext.lower()
	
	# removes everything except for letters this is used for calculating the healthiness
	ciphertext_only_letters = re.sub("[^a-z]+", "", ciphertext)

	alphabet = list("abcdefghijklmnopqrstuvwxyz")

	#randomly shuffles the alphabet
	random.shuffle(alphabet)
	starter_key = "".join(alphabet)	#starter key is random arrangement of alphabet

	# calculates the best keys and prints them out in a decending order of healthiness
	# highest healthiness (most correct) will be at the bottom
	best_keys = calculate_best_key(ciphertext_only_letters, starter_key, ciphertext)
	best_keys = sorted(best_keys)
	for i in range(len(best_keys)):
		print("================\n"+"Score:", best_keys[i][0], "\nKey:", best_keys[i][1], "\nDecryption:", substitution(ciphertext, best_keys[i][1]))
	# print(best_keys)

	#prints out the best guess
	#its just the last thing anyway
	print("\n======== BEST GUESS ========")
	print("Score:", best_keys[-1][0])
	print("Key:", best_keys[-1][1])
	print("Decryption:", substitution(ciphertext, best_keys[-1][1]))

def calculate_best_key(ciphertext_only_letters, starter_key, ciphertext):
	#creates object to calculate fitness
	calculator = create_nGramInfo_class()
	print("\n\n\nCiphertext:", ciphertext)
	print("Ciphertext Healthiness Score:", calculator.calculate_fitness_score(ciphertext))
	
	highest = []	#highest holds the highest scores and the keys associated with the scores
	
	# this is the key that is shuffled into a new key every iteration
	key = list('abcdefghijklmnopqrstuvwxyz')

	# if the thing cant be solved iterations should be increased first
	iteration = 0
	while iteration < 15:
		print("Iteration:", iteration)

		#generates new key and calculates the fitness of the keys associated possible plaintext
		random.shuffle(key)
		new_key = "".join(key)
		print("new key:", new_key)
		high_score = calculator.calculate_fitness_score(substitution(ciphertext_only_letters, new_key))
		best_key = new_key
		highest.append([high_score, best_key])

		i = 0
		
		# this can be increased if solver not solving however changing iteration number should be first
		while i < 10000:
			
			prev_key = new_key

			#generates 2 random numbers (musnt be the same)
			num1 = num2 = 0
			while num1 == num2:
				num1 = random.randint(0, 25)
				num2 = random.randint(0, 25)

			#swaps the letters
			new = list(new_key)
			new[num1], new[num2] = new[num2], new[num1]
			new_key = "".join(new)

			#creates the possible plaintext and calculates fitness
			plaintext = substitution(ciphertext_only_letters, new_key)
			new_score = calculator.calculate_fitness_score(plaintext)

			#if new score is higher than high score new score becomes high score and is added to highest list
			if new_score > high_score:
				high_score = new_score
				best_key = new_key
				highest.append([high_score, best_key])
				if len(highest) > 20:
					highest = sorted(highest)
					highest = highest[5:]
			else:	#if score doesnt increase it goes back to previous key
				new_key = prev_key

			i += 1

		# summarises information in every iteration
		print("Current highest score is", high_score, "on iteration", iteration)
		print(best_key)
		print("This decodes to", substitution(ciphertext_only_letters, best_key))
		print("\n\n")
		iteration += 1

	return highest

def create_nGramInfo_class():
	print("Enter '1' for monograms")
	print("Enter '2' for bigrams")
	print("Enter '3' for trigrams")
	print("Enter '4' for quadgrams")
	print("Note: quadgrams can only do analysis on messages >= 4 characters\ntrigrams for >= 3 and so on \n(if you need a program to help decipher a < 4 letter caesar cipher RIP)")
	mode = input("Enter Mode: ")
	mode = mode.strip().lower()

	if mode == '1':
		file_name = "ngrams/english_monograms.txt"
	elif mode == '2':
		file_name = "ngrams/english_bigrams.txt"
	elif mode == '3':
		file_name = "ngrams/english_trigrams.txt"
	elif mode == '4':
		file_name = "ngrams/english_quadgrams.txt"
	else: 
		print("Make sure input is correct")
		exit()

	return nGramInfo(file_name)


def substitution(ciphertext_only_letters, key):
	plaintext = ""
	for letter in ciphertext_only_letters:
		if letter.isalpha() == True:
			plaintext += key[ord(letter) - ord("a")]
		else:
			plaintext += letter

	return plaintext

if __name__ == "__main__":
	main()