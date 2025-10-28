class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        """

        l > r : 3 2 -> move left first = True
                    -> move right first =  False
        
        l == r = both works
        """

        r = sum(nums)
        l = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if abs(l - r) == 1:
                    ans +=1
                elif r == l:
                    ans += 2
            else:
                r -= nums[i]
                l += nums[i]
        return ans
