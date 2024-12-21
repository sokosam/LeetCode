class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        curr = ans
        for i in nums:
            if i >= curr and curr + i  < i :
                curr = i
            else:
                curr += i
            ans = max(ans,curr)
        return ans


# If we choose to add i, the resulting curr needs to be >= i