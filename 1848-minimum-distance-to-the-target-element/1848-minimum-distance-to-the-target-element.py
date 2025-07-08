class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        left = float('inf')
        right = float('inf')

        for i in range(len(nums)):
            if i <= start and nums[i] == target:
                left = i
            if i >= start and nums[i] == target:
                right = i
                break
        return min(abs(start - left), abs(start - right))