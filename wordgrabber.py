def load_words():
	with open('english-words/words_alpha.txt') as word_file:
		valid_words = set(word_file.read().split())

	return valid_words


if __name__ == '__main__':
	english_words = load_words()

	print(len(english_words))	#making sure the number of words is correct
	
	#finding the max length of words in this dictionary
	max_len = max(english_words, key=len)
	print(max_len)
	print(len(max_len))

	#creating a 2d array based on length
	words_by_len = []
	for i in range(len(max_len)):
		words_by_len.append(list())

	#seperating words by length
	for word in english_words:
		words_by_len[len(word) - 1].append(word)	# - 1 because indexes start at 0

	#writing words into a new file based on length
	file = open("words_alpha_removed_some_words.txt", "w")
	for a_list in words_by_len:
		for word in a_list:
			file.write(word + "\n")