class WordDistance:

    def __init__(self, wordsDict: List[str]):
        cnt = 0
        self.lastSeen = defaultdict(list)
        for word in wordsDict:
            self.lastSeen[word].append(cnt)
            cnt += 1

    def shortest(self, word1: str, word2: str) -> int:
        """
        0 5
        3 7
        """ 

        arr = self.lastSeen[word2]
        best = float('inf')
        for index in self.lastSeen[word1]:
            val = bisect_right(arr, index)
            if val == 0:
                best = min(best, abs(arr[0] - index))
            elif val == len(arr):
                best = min(best, abs(arr[-1] - index))
            else:
                best = min(best, abs(arr[val] - index))
                best = min(best, abs(arr[val - 1] - index))
        return best




# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)