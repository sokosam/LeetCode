class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        h = []
        m = Counter(nums)
        maxSize = max(m.values())
        return  len(nums)//maxSize >= k