class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        

        if len(nums) == 1:
            return 0


        l= 0
        r = len(nums) -1
        while l <=r:
            m = (l + r)//2

            if m == len(nums) -1:
                if nums[m] > nums[m - 1]:
                    return m
                else:
                    r = m -1
            elif m == 0:
                if nums[m] > nums[m + 1]:
                    return m
                else:
                    l = m + 1
            else:
                if nums[m] > nums[m -1] and nums[m] > nums[m + 1]:
                    return m
                if nums[m - 1] > nums[m]:
                    r = m -1
                else:
                    l = m + 1
        return - 1