#caesar cipher solver using dictionary matching

from wordgrabber import *
import re

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

# prints out all of the combination just in case you want to 
# manually read through them to find the message
print("------( All Combinations )------")
print("Shift:   Message")
for i in range(26):
	print('{:>5d}: "{}"'.format(i, all_shifts[i]))
print("--------------------------------")

#grabs all the english words
english_words = load_words_shortened_apostrophe()

#finds length of the cipher text
ciphertext_word_len = len(ciphertext.split())

#list that lists the number of correct words in a deciphered message
correct_count = []

#counts the correct words and appends it to correct_count
for phrase in all_shifts:
	words = phrase.split()
	correct = 0
	for word in words:
		# if word is not fully alphabetical then 
		# remove all non alphabetical characters excluding "'"
		if word.isalpha == False:
			word = re.sub("[^a-zA-Z' ]+", "", word)
		if word in english_words:
			correct += 1

	correct_count.append(correct)

all_correct = False	#flag: if false there are no messages that have all words correct
for i in range(26):
	if correct_count[i] == ciphertext_word_len:
		print("---- (The following message(s) has all valid words) ----")
		print("Message: ", all_shifts[i])
		print("Shift value:", i)
		print("--------------------------------------------")
		all_correct = True

if all_correct == False:
	print("No exact match has been found the following are the best guesses")
	for i in range(26):
		if correct_count[i] == max(correct_count):
			print("Message: ", all_shifts[i])
			print("Shift value:", i)