class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(nums[i] + prefix[i])

        count = 0

        for i in range(0, len(nums) -1):
            if prefix[i + 1] >= prefix[-1] - prefix[i + 1]:
                count +=1
        return count