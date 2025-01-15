class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prev = 0

        ans = 0
        curr = 0

        for i in nums:
            if i <= prev:
                curr = i
            else:
                curr += i
            prev = i
            ans = max(ans, curr)
        return ans