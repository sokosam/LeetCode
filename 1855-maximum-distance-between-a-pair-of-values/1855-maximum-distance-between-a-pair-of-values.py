class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        ptr2 = 0
        farthest = 0

        for i in range(len(nums1)):
            n1 = nums1[i]
            
            while ptr2 < len(nums2) and nums2[ptr2] >= n1 :
                ptr2 += 1
            farthest = max(farthest, ptr2 - i - 1)
        return farthest