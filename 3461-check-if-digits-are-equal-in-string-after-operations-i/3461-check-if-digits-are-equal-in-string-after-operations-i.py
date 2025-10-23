class Solution:
    def hasSameDigits(self, s: str) -> bool:
        

        nums = [int(i) for i in s]

        while len(nums) > 2:
            nums = [(nums[i] + nums[i -1 ])%10 for i in range(1,len(nums))]
        return nums[0] == nums[-1]