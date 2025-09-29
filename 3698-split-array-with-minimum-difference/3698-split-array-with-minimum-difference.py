class Solution:
    def splitArray(self, nums: List[int]) -> int:
        

        def findMaxIndex(nums):
            best = 0
            for i in range(len(nums)):
                if nums[i] > nums[best]:
                    best = i
            return best
        
        def checkIncreasing(nums):

            for i in range(1, len(nums)):
                if nums[i] <= nums[i-1]:
                    return False
            return True
        

        splitIndex = findMaxIndex(nums)
        best = -1

        if checkIncreasing(nums[0: splitIndex + 1]):
            right = nums[splitIndex + 1:]
            right.reverse()
            if checkIncreasing(right):
                best = abs(sum(nums[0: splitIndex + 1]) - sum(right))

        
        if checkIncreasing(nums[0 :splitIndex]):
            right = nums[splitIndex :]
            right.reverse()

            if checkIncreasing(right):
                best = abs(sum(nums[0: splitIndex ]) - sum(right)) if best == -1 else min(best, abs(sum(nums[0: splitIndex ]) - sum(right)))
        return best
