class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        

        curr = 0
        ans = 0
        for index, i in enumerate(values):
            curr -= 1
            ans = max(curr + i, ans)
            if i > curr:
                curr = i
                if index > 0:
                    ans = max(ans,curr)
                

        return ans
