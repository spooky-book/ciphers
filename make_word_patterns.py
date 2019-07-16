from wordgrabber import *

def grab_create_all_word_pattern():
	english_words = load_words_common()
	# english_words = load_words_shortened()

	pattern_dict = {}
	for word in english_words:
		pattern = create_word_pattern(word)
		if pattern not in pattern_dict:
			pattern_dict[pattern] = [word]
		else:
			pattern_dict[pattern].append(word)

	return pattern_dict

	# for i in pattern_dict:
	# 	print(i, pattern_dict[i])


#takes in a string and returns the word pattern
def create_word_pattern(word):
	word = word.strip()
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

	return word_pattern