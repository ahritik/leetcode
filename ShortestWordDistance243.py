'''
243. Shortest Word Distance

Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
'''

def shortestDistance(words, word1, word2):
    i1, i2 = -1, -1
    res = len(words)
    for i in range(len(words)):
        if words[i] == word1:
            i1 = i
        elif words[i] == word2:
            i2 = i
        if i1 != -1 and i2 != -1:
            res = min(res, abs(i1 - i2))
    return res