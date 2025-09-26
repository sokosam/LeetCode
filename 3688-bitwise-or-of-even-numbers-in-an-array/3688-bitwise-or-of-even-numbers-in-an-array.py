class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        x = [i for i in nums if i %2 == 0]
        if len(x) == 0:
            return 0
        ans = x[0]
        for i in range(1, len(x)):
            ans |= x[i]
        return ans