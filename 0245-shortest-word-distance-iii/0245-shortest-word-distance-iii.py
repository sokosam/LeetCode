class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        lastSeen1 = -1
        lastSeen2 = -1
        best = float('inf')
        for index, word in enumerate(wordsDict):
            if word == word1:
                if word1 == word2 and lastSeen1 != -1:
                    best = min(best, index - lastSeen1)
                if lastSeen2 != -1:
                    best = min(best, index - lastSeen2)
                lastSeen1 = index
            elif word == word2:
                if lastSeen1 != -1:
                    best = min(best, index - lastSeen1)
                lastSeen2 = index
        return best