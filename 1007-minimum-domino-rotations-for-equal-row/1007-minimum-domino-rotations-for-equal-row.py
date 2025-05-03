class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        ans = -1
        curr = 0
        for i in range(1, 7):
            accepted = True
            for j in range(len(tops)):
                if tops[j] == i:
                    continue
                if bottoms[j] == i:
                    curr += 1
                    continue
                accepted = False
                break
            if accepted:
                if ans == -1:
                    ans = curr
                else:
                    ans = min(ans,curr)
                curr = 0
        return ans

