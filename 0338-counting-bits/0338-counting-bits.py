class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0,1]
        """
        0 1 2 3 4 5 6 7 8
        0 1 1 2 1 2 2 3 1
        """
        if n == 0:
            return [0]
        bound = 2
        curr = 0
        for i in range(2, n + 1):
            if i == bound:
                bound*=2
                ans.append(1)
                curr = 0
            else:
                ans.append(1 + ans[curr])
            curr += 1
        return ans
