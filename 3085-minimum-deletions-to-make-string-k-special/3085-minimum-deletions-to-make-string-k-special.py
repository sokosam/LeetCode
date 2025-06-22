class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        """

        keep track of all frequencies
        aabcaba
        a : 4 b: 2 c : 1
        k = 0
        1 2 2 4 4 4 4
        1 1 1 2 2 3 4

        dabdcbdcdcd
        a : 1 b : 2 c : 3 d : 5
        1 1 1 1 2 2 2 3 3 4 5


        """

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