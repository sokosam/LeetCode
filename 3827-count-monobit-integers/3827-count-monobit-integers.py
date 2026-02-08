class Solution:
    def countMonobit(self, n: int) -> int:
        
        if n == 0:
            return 1
        if n == 1:
            return 2

        
        curr = 1
        shift = 0

        while curr - 1 <= n:
            curr <<= 1
            shift +=1
        return shift 
        
