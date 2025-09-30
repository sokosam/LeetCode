class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        return  len(nums)// max(Counter(nums).values()) >= k