# Completed on: 9/15/2024
# Submission: https://leetcode.com/problems/two-sum/submissions/1391530556/
# Time Complexity: O(n)
# Space Complexity: O(n) 
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        memoi = {}
        for i in range(len(nums)):
            if target - nums[i] in memoi: return [memoi[target- nums[i]], i]
            else: memoi[nums[i]] = i