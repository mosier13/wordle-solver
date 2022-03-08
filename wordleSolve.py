"""
Author: Kyle J Mosier
github.com/mosier13
Wordle Solver Program
"""

allWords = []
guesses = []
mysteries = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

frequencies = {}

frequencies['A'] = 0.0834
frequencies['B'] = 0.0154
frequencies['C'] = 0.0273
frequencies['D'] = 0.0414
frequencies['E'] = 0.1260
frequencies['F'] = 0.0203
frequencies['G'] = 0.0192
frequencies['H'] = 0.0611
frequencies['I'] = 0.0671
frequencies['J'] = 0.0023
frequencies['K'] = 0.0087
frequencies['L'] = 0.0424
frequencies['M'] = 0.0253
frequencies['N'] = 0.0680
frequencies['O'] = 0.0770
frequencies['P'] = 0.0166
frequencies['Q'] = 0.0009
frequencies['R'] = 0.0568
frequencies['S'] = 0.0611
frequencies['T'] = 0.0937
frequencies['U'] = 0.0285
frequencies['V'] = 0.0106
frequencies['W'] = 0.0234
frequencies['X'] = 0.0020
frequencies['Y'] = 0.0204
frequencies['Z'] = 0.0006

def getAllWords():
	reader = open('five-letter-words.txt', 'r')
	words = reader.read().split(" ")
	reader.close()
	return words 

def addWord(word):
	if word not in allWords:
		word = word.upper()
		writer = open('five-letter-words.txt', 'a')
		writer.write(" " + word)
		writer.close()
		allWords.append(word)
		print("wordleSolve: Added word '" + word + "' to the word list")
	else:
		print("wordleSolve: " + word + " is already in the word list")

def getGuess():
	word = input("wordleSolve >>> Enter the five-letter guess word: ").upper()
	wordStatus = input("wordleSolve >>> Enter a five-letter GYB string for the status of that guess. For each char in the GYB string, enter G if wordle said that letter was completely correct, Y if wordle said that letter is in the wrong place but in the word, and B if the letter is not part of the word: ").upper()

	if(len(word) == len(wordStatus) and len(word) == 5):
		guess = word + wordStatus
		guesses.append(list(guess))
	else:
		print("wordleSolve: ERROR: Words must be of length 5")

def testWord(word_as_list, guesses):
	possible = True
	for guess in guesses:
		if(guess != None):
			for i in range(5):
				#print(guess[i])
				if(guess[i] in mysteries):
					#print("[debug] removing letter " + guess[i] + " from mysteries")
					mysteries.remove(guess[i])
				if(guess[i+5] == 'G' and word_as_list[i] != guess[i]):
					possible = False
				elif(guess[i+5] == 'Y' and (guess[i] not in word_as_list or word_as_list[i] == guess[i])):
					possible = False
				elif(guess[i+5] == 'B' and guess[i] in word_as_list):
					possible = False
	return possible

def getPossibleWords():
	possibleWords = []
	for word in allWords:
		possible = True
		word_as_list = list(word)
		if testWord(word_as_list, guesses):
			possibleWords.append(word)

	return possibleWords

def getLetterFrequency(letter):
	return frequencies[letter]

def getWordFrequency(word):
	freq = 0
	for letter in mysteries:
		if letter in word:
			freq += getLetterFrequency(letter)
	return freq


allWords = getAllWords()
guesses = []


while True:
	command = input("wordleSolve >>> ")
	#print(command.upper())
	if(command.upper() == "CLEAR"):
		guesses = []
		mysteries = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	elif(command.upper() == "ADD"):
		word = input("wordleSolve >>> Input word to add: ").upper()
		if(len(word) != 5):
			print("wordleSolve: ERROR: Words must be of length 5")
		else:
			addWord(word)
	elif(command.upper() == "GUESS"):
		getGuess()
		print("wordleSolve: Guess logged. Enter SHOW to see possible words")
	elif(command.upper() == "SHOW"):
		possibleWords = getPossibleWords()
		numWords = len(possibleWords)
		for word in possibleWords:
			if(getWordFrequency(word) > 0.3):
				print(word + "%10.4f" % (getWordFrequency(word)))
		print("wordleSolve: We found " + str(numWords) + " possible words from our list...")
		print()
		print("wordleSolve: Remaining mystery letters:", "".join(mysteries))
	elif(command.upper() == "INVENTORY"):
		print("wordleSolve: The current size of the word list is " + str(len(allWords)))
	elif(command.upper() == "EXIT"):
		exit()
	else:
		print("wordleSolve: That is not a valid command. Try CLEAR, ADD, GUESS, SHOW, INVENTORY, or EXIT")


#print(guesses)
#guesses.append(getGuess())
#print(guesses)
#print(getPossibleWords())

#print(testWord(list("DOGGO"), [['D', 'O', 'N', 'U', 'T', 'G', 'G', 'B', 'B', 'B']]))


#print(getWordFrequency("AROSETUNIC"))

"""
possibleWords = getPossibleWords()
numWords = len(possibleWords)
for word in possibleWords:
	for other_word in possibleWords:
		if(getWordFrequency(word + other_word) > 0.73 and word != other_word):
			print(word + "" + other_word + "%10.4f" % (getWordFrequency(word + other_word)))
"""