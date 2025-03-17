class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        x = 0

        for i in nums:
            x ^= i

        return x == 0