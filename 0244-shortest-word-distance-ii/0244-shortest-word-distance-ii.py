class WordDistance:

    def __init__(self, wordsDict: list[str]):
        self.wordIndexes = defaultdict(list)
        for index,word in enumerate(wordsDict):
            self.wordIndexes[word].append(index)
        

    def shortest(self, word1: str, word2: str) -> int:

        word1 = self.wordIndexes[word1]
        word2 = self.wordIndexes[word2]

        word1_ptr = 0
        diff = float('inf')
        for index in word2:
            while word1_ptr < len(word1) - 1 and index > word1[word1_ptr]:
                word1_ptr +=1 

            if word1_ptr != 0:
                diff = min(diff, abs(word1[word1_ptr - 1] - index))
            
            diff = min(diff, abs(word1[word1_ptr] - index))
        
        return diff
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)