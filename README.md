# Ciphers Solvers
We have different python programs that implement basic ciphers and then solve them using different methods.  
## Caesar
### caesar_cipher.py
- implementation of the caesar cipher basically shifts letters in the message by a specified amount

### caesar_cipher_solver_dict.py
- solves caesar cipher using a dictorary method
- creates all potential messages from the cipher text by shifting the letters by 1 - 26 steps and tries to match up the words with the dictionary
- the more words from the potential cipher text that can be found the more likely the message is correct
- doesnt work without spaces

### caesar_cipher_solver_frequency_analysis_v2.py
- solves caesar cipher using a frequency analysis method
- creates all potential messages from the cipher text and finds a "fitness score" for each message
- fitness score is based of using ngrams to measure how "english" the message is
- words without spaces as well

## Substitution 
### substitution_cipher.py
- implementation of the substitution cipher in python, where every instance of a letter will be replaced with another letter
- once a letter has been used then it cannot be used again

### substitution_cipher_solver_frequency_analysis.py
- decrypts ciphertext encrypted using the substitution cipher
- basically randomly guesses a substitution key and measures its correctness using the fitness score
- generates future random guesses off the best keys previously guessed
- increasing the number of iterations which the program runs for will increase its success rate
- works with spaces or without spaces between the words, words with minor mispellings as well
- works well with longer messages

# References
30k_most_common_words.txt
  https://github.com/derekchuank/high-frequency-vocabulary

words_alpha_* 
  files derived from words_alpha.txt in folder english-words
  
folder english-words
  cloned from https://github.com/dwyl/english-words
  
english_* files in folder ngrams
  from http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/#a-python-implementation
  
