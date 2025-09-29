class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        best = 0
        while l < r:
            best = max(best, nums[l] + nums[r])
            r -=1
            l +=1
        return best
