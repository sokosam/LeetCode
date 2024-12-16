class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        memoi = {}
        for i in range(len(nums)):
            if target - nums[i] in memoi: return [memoi[target- nums[i]], i]
            else: memoi[nums[i]] = i