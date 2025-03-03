class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        minElement = float('inf')
        sumAmt = 0
        
        for i in nums:
            if i != 0:
                minElement=min(minElement,i)
                sumAmt += i
        
        times = 0

        while sumAmt > 0:
            newMin = float('inf')
            for i in range(len(nums)):
                if nums[i] != 0:
                    sumAmt -= minElement
                    nums[i] -= minElement
                    if nums[i] != 0:
                        newMin = min(newMin, nums[i])
            minElement = newMin
            times +=1
 
        return times