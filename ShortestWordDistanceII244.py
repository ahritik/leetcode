'''
243. Shortest Word Distance II

Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.
Implement the WordDistance class:
    WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
    int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.  
'''

class WordDistance:
    def __init__(self, wordsDict):
        self.dict = {}
        for i, word in enumerate(wordsDict):
            if word not in self.dict:
                self.dict[word] = []
            self.dict[word].append(i)
    
    def shortest(self, world1, world2):
        i1, i2 = self.dict[world1], self.dict[world2]
        res = len(self.dict)
        
        for i in i1:
            for j in i2:
                res = min(res, abs(i-j))
        return res