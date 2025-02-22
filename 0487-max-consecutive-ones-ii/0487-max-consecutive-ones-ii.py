class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        secondLast = -1
        last = -1
        best = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                if last == -1:
                    last = i
                else:

                    if secondLast == -1:
                        best = i 
                    else:
                        best = max(best, i - secondLast - 1)
                    secondLast = last
                    last = i
            elif i == len(nums) - 1:
                best = max(best, i - secondLast )

        
        if secondLast == -1 or last == -1:
            return len(nums)
        else:
            return best

        