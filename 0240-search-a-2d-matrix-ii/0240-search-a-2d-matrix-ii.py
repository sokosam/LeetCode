class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binSearch(nums, target):
            r = len(nums) -1
            l = 0
            while l <=r:
                m = l  +(r-l)//2
                if nums[m] == target:
                    return True
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False
        for row in matrix:
            if binSearch(row, target):
                return True
        return False
