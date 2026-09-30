class WordDistance:

    def __init__(self, wordsDict: list[str]):
        self.indexes =  defaultdict(list)
        # self.distances = defaultdict(int)
        for index, word in enumerate(wordsDict):
            self.indexes[word].append(index)


    def shortest(self, word1: str, word2: str) -> int:
        word2_indexes = self.indexes.get(word2, [])
        word1_indexes = self.indexes.get(word1, [])

        if len(word2_indexes) == 0 or len(word1_indexes) == 0:
            return -1
        
        best = float('inf')
        for index in word1_indexes:
            placement = bisect_right(word2_indexes, index)

            if placement == len(word2_indexes):
                placement -= 1
            left = placement - 1
            right = placement

            diff = abs(word2_indexes[left] - index)
            best = min(best, diff)

            if right < len(word2_indexes):
                diff = abs(word2_indexes[right] - index)
                best = min(best, diff)
        return best





        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)