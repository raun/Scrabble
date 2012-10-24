import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    for letter in word:
    	score += SCRABBLE_LETTER_VALUES[letter]
    score = score * len(word)
    if len(word) ==  n:
    	score = score +50
    return score

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    handcopy=hand.copy()
    for char in word:
    	if char not in handcopy or handcopy[char]<=0:
    		return False
    	else:
    		handcopy[char] -=1
    if word in wordList:
    	return True
    return False
  
def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all possible 
    permutations of lengths 1 to HAND_SIZE.

    If all possible permutations are not in wordList, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    maximum=0
    bestWord=None
    for word in wordList:
    	if isValidWord(word,hand,wordList):
    		if maximum < getWordScore(word,HAND_SIZE):
    			maximum = getWordScore(word,HAND_SIZE)
    			bestWord = word
    return bestWord

HAND_SIZE=7
wordList = loadWords()

print str(compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList))
print str(compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList))
print str(compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList))
print str(compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList))
