class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.


        1 2 3
        1 3 2


        1 2 3 4
        1 2 4 3

        1 2 4 3
        1 3 2 4 

        1 4 3 2

        2 1 3 4


        1 3 5 4 2
        6 1 3 5 4 2
        """
        

        if len(nums) == 1: return nums
        last = -1 

        for i in range(1, len(nums)):
            curr = nums[i]
            if curr > nums[i - 1]:
                last = i - 1
        
        def reverse(nums, l = 0, r = len(nums) - 1):

            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -=1
            

        if last == -1:
            reverse(nums)
        else:
            mi = -1
            for i in range(last + 1, len(nums)):
                if nums[i] > nums[last]:
                    if mi == -1:
                        mi = i
                    elif nums[i] <= nums[mi]:
                        mi = i
            if mi == -1:
                reverse(nums)
                return

            nums[last], nums[mi] = nums[mi], nums[last]
            reverse(nums, last + 1)

