class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        m = Counter(nums)

        return max([-1] + [i for i in m if m[i] == 1])