
#
#
# Problem #6: Computer chooses a word
#
#
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
    	if ps4a.isValidWord(word,hand,wordList):
    		if maximum < ps4a.getWordScore(word,HAND_SIZE):
    			maximum = ps4a.getWordScore(word,HAND_SIZE)
    			bestWord = word
    return bestWord
