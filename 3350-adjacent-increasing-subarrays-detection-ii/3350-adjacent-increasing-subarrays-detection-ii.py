class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        def check(nums, k):
            start = 0
            arrs = set()
            if k ==1:
                return len(nums) > 0
            for end in range(1,len(nums)):
                if nums[end] <= nums[end - 1]:
                    start = end
                if end - start +1  >= k:
                    arrs.add(start)
                    start +=1
            for i in arrs:
                if i - k in arrs:
                    return True
            return False
        l = 0
        r = len(nums) - 1
        best =0
        while l <=r:
            m = (l+r)//2
            if check(nums, m):
                l = m + 1
                best= m
            else:
                r = m -1
        return best

