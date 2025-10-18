class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        '''

            4 44 4
            3 4 
            3
        '''

        minAmt = min(nums) - k
        nums.sort()
        ans = 0
        for i in nums:
            smallest = i - k
            largest = i + k
            if smallest <= minAmt <= largest   :
                ans +=1
                minAmt +=1
            elif smallest > minAmt:
                minAmt = smallest + 1
                ans +=1
        return ans

