class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

            if the array is rotated, nums[0] > nums[-1]

        """

        def binSearch(target, nums):
            
            l = 0
            r = len(nums) -1 
            while l<=r:
                m = l + (r-l)//2

                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m -1 
                else:
                    l = m + 1
            return -1

        if nums[0] <= nums[-1]:
            return binSearch(target, nums)

       
        def findPivot(nums):
            maxElement = nums[0]
            index = -1
            l = 0
            r = len(nums) - 1
            while l<=r:
                m = l + (r-l)//2
                if nums[m] >= maxElement:
                    maxElement = nums[m]
                    index = m
                    l = m + 1
                else:
                    r = m - 1
            return index
        pivot = findPivot(nums)
        print(pivot)

        left = binSearch(target,nums[0: pivot + 1])
        right = -1
        if binSearch(target, nums[pivot+1:]) >= 0:
            right = pivot + 1 + binSearch(target, nums[pivot+1:])
        return max(left, right)
            
