class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        

        l = 0
        r = len(nums) - 1
        closestNeg = -1

        while l <=r:
            m = l + (r -l)//2

            if nums[m] < 0:
                closestNeg = m
                l = m + 1
            else:
                r = m - 1
        l = 0
        r = len(nums) - 1
        closestPos = -1
        while l <=r:
            m = l + (r -l)//2

            if nums[m] > 0:
                closestPos = m
                r = m -1
            else:
                l = m + 1
        print(closestNeg, closestPos)

        pos = len(nums) - closestPos if closestPos >= 0 else 0
        
        return max(closestNeg + 1, pos )

                
