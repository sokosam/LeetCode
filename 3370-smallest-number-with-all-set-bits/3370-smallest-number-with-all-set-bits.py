class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1 
        while x < n:
            x*=2
            x+=1
        return x