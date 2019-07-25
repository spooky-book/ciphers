import re, random, pdb

from ngram_class import nGramInfo

#substitution cipher

def main():
	ciphertext = input("Enter the message: ")
	ciphertext = ciphertext.lower()
	
	ciphertext_only_letters = re.sub("[^a-z]+", "", ciphertext)

	#print(ciphertext_only_letters)

	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	#print(alphabet)
	#randomly shuffles the alphabet
	random.shuffle(alphabet)
	#print(alphabet)

	#starter key is random arrangement of alphabet
	starter_key = "".join(alphabet)
	print(starter_key)

	best_keys = calculate_best_key(ciphertext_only_letters, starter_key, ciphertext)
	best_keys = sorted(best_keys)
	print(best_keys)

def calculate_best_key(ciphertext_only_letters, starter_key, ciphertext):
	
	#creates object to calculate fitness
	calculator = create_nGramInfo_class()

	#creates a possible plaintext with the starter key
	plaintext = substitution(ciphertext_only_letters, starter_key)
	high_score = calculator.calculate_fitness_score(plaintext)
	best_key = starter_key
	print("plaintext:", plaintext, "\nstarter_key:", starter_key, "\nciphertext_only_letters:", ciphertext_only_letters)

	highest = [[high_score, best_key]]
	print(high_score)
	
	new_key = starter_key

	#seen = set()
	#seen.add(starter_key)

	iteration = 0
	while iteration < 200:
		random.shuffle(list(new_key))
		new_key = "".join(new_key)
		
		print(new_key)
		#seen.add(new_key)

		iteration += 1
		i = 0
		
		while i < 10000:
			
			num1 = num2 = 0
			while num1 == num2:
				num1 = random.randint(0, 25)
				num2 = random.randint(0, 25)

			new = list(new_key)
			new[num1], new[num2] = new[num2], new[num1]

			new_key = "".join(new)

			#if new_key in seen:
			#	continue
			#print(new_key)

			plaintext = substitution(ciphertext_only_letters, new_key)
			new_score = calculator.calculate_fitness_score(plaintext)
			print(new_score)
			#seen.add(new_key)

			if new_score > high_score:
				high_score = new_score
				best_key = new_key
				highest.append([high_score, best_key])
				#print("yeet")
			
			i += 1
		pdb.set_trace()
		print("Current highest score is", high_score, "on iteration", iteration)
		print(best_key)
		print("This decodes to", substitution(ciphertext_only_letters, best_key))

	#print(seen)
	#print(len(seen))

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
		plaintext += key[ord(letter) - ord("a")]

	return plaintext

if __name__ == "__main__":
	main()