class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        

        if len(nums) == 1:
            return 0
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = l + (r-l)//2

            val = nums[m]
            left = False
            if m -1 < 0 or nums[m-1] < nums[m]:
                left = True
            right = False
            if  m + 1 >= len(nums) or nums[m + 1] < nums[m]:
                right = True
            
            if left and right:
                return m
            elif left:
                l = m + 1
            else:
                r = m - 1


        return -1