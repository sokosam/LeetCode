class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        heapq.heapify(nums1)
        nums2 = [-i for i in nums2]
        heapq.heapify(nums2)

        ans = 0
        while nums1:
            ans += heapq.heappop(nums1)*-1*heapq.heappop(nums2)
        return ans