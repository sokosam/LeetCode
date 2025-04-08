class Solution:
    def minimumSteps(self, s: str) -> int:
        
        swaps = 0
        cnt = 0

        for i in s:
            if i == "1":
                cnt+=1
            else:
                swaps += cnt
        return swaps
                