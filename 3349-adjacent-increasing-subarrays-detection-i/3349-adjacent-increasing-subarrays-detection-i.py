class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
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

