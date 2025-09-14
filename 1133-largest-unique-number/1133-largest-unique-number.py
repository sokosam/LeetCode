class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        return (lambda x : max([-1] + [i for i in x if x[i] == 1]))(Counter(nums))
