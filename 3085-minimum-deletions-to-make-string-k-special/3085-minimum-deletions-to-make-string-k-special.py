class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        d = Counter(word)
        bound = max(d.values())
        check = len(word)
        best = float('inf')
        for i in range(bound + 1):
            count = 0
            for item in d:
                if i <= d[item] <= i + k:
                    count += d[item]
                elif d[item] > i + k:
                    count += i + k
            best = min(best, check - count)
        best = min(best, check - bound)
        return best