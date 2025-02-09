class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        m = {}
        badPairs = 0
        for i in range(len(nums)):
            val = i - nums[i]
            
            goodPairs = m[val] if val in m else 0
            badPairs += i - goodPairs
            if val in m:
                m[val] +=1
            else:
                m[val]  = 1
        return badPairs
