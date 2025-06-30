class Solution:
    def findLHS(self, nums: List[int]) -> int:
        m = Counter(nums)
        ans = 0
        for key in m:
            val = m[key]
            if key - 1 in m:
                ans = max(ans, m[key-1] + val)
            if key + 1 in m:
                ans = max(ans, m[key + 1] + val)
        return ans