class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        

        def find_farthest(nums, curr):
            l = 0
            r = len(nums) - 1
            farthest = 0
            while l <= r:
                m = l + (r-l)//2
                if nums[m] >= curr:
                    l = m +1 
                    farthest = m
                else:
                    r = m - 1

            return farthest



        best = 0
        for i in range(len(nums1)):
            val = nums1[i]

            farthest = find_farthest(nums2, val)
            if farthest >= i:
                best = max(best, farthest-i)
        return best