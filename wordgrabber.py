def load_words_all():
	with open('english-words/words_alpha.txt') as word_file:
		valid_words = set(word_file.read().split())

	return valid_words

def load_words_shortened():
	with open('words_alpha_removed_some_words.txt') as word_file:
		valid_words = set(word_file.read().split())

	return valid_words

def load_words_shortened_apostrophe():
	with open('words_alpha_removed_some_words_added_apostrophes.txt') as word_file:
		valid_words = set(word_file.read().split())

	return valid_words

def sort_words_length(english_words):
	#finding the max length of words in this dictionary
	max_len = max(english_words, key=len)
	#print(max_len)
	#print(len(max_len))

	#creating a 2d array based on length
	words_by_len = []
	for i in range(len(max_len)):
		words_by_len.append(list())

	#seperating words by length
	for word in english_words:
		words_by_len[len(word) - 1].append(word.lower())	# - 1 because indexes start at 0

	return words_by_len

if __name__ == '__main__':
	english_words = load_words_shortened()

	print(len(english_words))	#making sure the number of words is correct
	
	words_by_len = sort_words_length(english_words)	

	#writing words into a new file based on length
	file = open("words_alpha_removed_some_words_added_apostrophes.txt", "w")
	for word in english_words:
		file.write(word.lower() + "\n")