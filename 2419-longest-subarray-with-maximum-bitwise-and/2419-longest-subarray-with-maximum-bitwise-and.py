class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0
        best = 0
        strongest = max(nums)
        for i in range(len(nums)):
            if i == 0 and nums[i] == strongest:
                count +=1
            elif strongest == nums[i] and nums[i] == nums[i -1]:
                count +=1
            elif strongest == nums[i]:
                count = 1
            else:
                count = 0
            best = max(best,count)
        return best 