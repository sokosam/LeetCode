class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        mi = nums[0]
        ans = 1
        for i in range(len(nums)):
            if abs(mi - nums[i]) > k:
                ans +=1
                mi = nums[i]
        return ans