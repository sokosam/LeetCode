class Solution:
    def check(self, nums: List[int]) -> bool:
        
        foundDecrease = False
        prev = -1 
        ceil = -1
        for i in nums:
            if i < prev:
                if not foundDecrease:
                    foundDecrease = True
                    ceil = prev
                else:
                    return False
            if i > ceil and foundDecrease:
                return False
            prev = i


        return True