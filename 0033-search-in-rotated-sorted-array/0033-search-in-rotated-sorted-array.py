class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binSearch(nums, target):
            l = 0
            r = len(nums) - 1
            while l <= r:
                m = (l + r) //2

                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        
        if nums[0] < nums[len(nums) - 1]: return binSearch(nums, target)
        l = 0
        r = len(nums) - 1
        m = 0
        while l < r:
            leftMost = nums[l]
            rightMost = nums[r]
            m = (l + r)//2

            if r - l == 1:
                m = l
                break            
            if leftMost > nums[m]:
                r = m 
            if rightMost < nums[m]:
                l = m 
        left = binSearch(nums[0: m + 1], target)
        right = binSearch(nums[m+1 :], target)
        if right != -1:
            right += m + 1
        return max(left,right)
            