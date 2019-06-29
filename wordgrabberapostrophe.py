def load_words():
	with open('english-words/words.txt') as word_file:
		valid_words = set(word_file.read().split())

	return valid_words


if __name__ == '__main__':
	english_words = load_words()

	print(len(english_words))	#making sure the number of words is correct

	#creating a 2d array based on length
	words_with_apostrophe = []

	#seperating words by length
	for word in english_words:
		if "'" in word:
			words_with_apostrophe.append(word)

	#writing words into a new file based on length
	file = open("words_with_apostrophe.txt", "w")
	for word in words_with_apostrophe:
		file.write(word + "\n")