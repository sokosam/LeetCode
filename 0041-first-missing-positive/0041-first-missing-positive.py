class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        foundOne = False
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 1
            elif nums[i] == 1:
                foundOne = True
        if not foundOne:
            return 1


        for i in range(len(nums)):
            if abs(nums[i]) - 1 < len(nums) and abs(nums[i]) -1 >= 0:
                if nums[abs(nums[i]) -1] > 0:
                    nums[abs(nums[i]) - 1] *= -1
        print(nums)
        i = 0
        while i < len(nums) and nums[i] < 0:
            i +=1
        return i + 1