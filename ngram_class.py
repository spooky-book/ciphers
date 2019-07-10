import math

#http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/
#inspired by above website

class nGramInfo():
	def __init__(self, filename):
		self.ngram_list = self.grab_ngrams(filename)
		self.total_samples = self.grab_total_samples(self.ngram_list)
		self.ngram_dict_prob = self.create_ngram_probability(self.ngram_list)
		self.floor = math.log10(0.01/self.total_samples)
		self.n_letters = len(self.ngram_list[0][0])
	
	def grab_ngrams(self, filename):
		f = open(filename, mode='r')

		ngrams = []

		for line in f:
			info = line.lower().split()
			info[1] = int(info[1])
			ngrams.append(info)
		
		f.close()

		return ngrams

	def grab_total_samples(self, ngram_list):
		total = 0
		for gram in ngram_list:
			total += gram[1]

		return total

	def create_ngram_probability(self, ngrams):
		ngram_dict = {}

		total_samples = float(0)

		for key, value in ngrams:
			ngram_dict[key] = math.log10(float(value)/self.total_samples)

		return ngram_dict

	def calculate_fitness_score(self, string):
		fitness_score = 0
		for i in range(len(string) - self.n_letters + 1):
			if string[i: i+self.n_letters] in self.ngram_dict_prob:
				#print("yes", string[i: i+self.n_letters])
				fitness_score += self.ngram_dict_prob[string[i: i+self.n_letters]]
			else:
				fitness_score += self.floor
				#print("no ", string[i: i+self.n_letters])

		return fitness_score