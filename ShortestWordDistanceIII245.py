'''
245. Shortest Word Distance III

Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.
'''

def shortestWordDistance(wordsDict, word1, word2) -> int:
    w1, w2 = [], []
    minDiff = len(wordsDict)
    for i in range(len(wordsDict)):
        if wordsDict[i] == word1:
            w1.append(i)
        if wordsDict[i] == word2:
            w2.append(i)

    for i in w1:
        for j in w2:
            if i != j:
                minDiff = min(minDiff, abs(i - j))
                
    return minDiff