class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        

        def helper(l, curr, ans):
            while l < len(nums):
                if nums[l] < 0 and curr + nums[l] < 0:
                    ans +=1
                elif nums[l] < 0 and curr + nums[l] ==0:
                    return min(helper(l +1, 0, ans ), helper(l +1, curr, ans + 1))
                else:
                    curr += nums[l]
                l += 1
            return ans
        
        return helper(0, 0, 0)
