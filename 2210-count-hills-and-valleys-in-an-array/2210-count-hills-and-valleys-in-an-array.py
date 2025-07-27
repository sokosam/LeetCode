class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0

        x = []
        for i in range(len(nums)):
            
            if i == 0 or  nums[i -1] != nums[i]:
                x.append(nums[i])
        
        nums = x
        for i in range(1,len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                ans += 1 
            if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                ans += 1 
        return ans 