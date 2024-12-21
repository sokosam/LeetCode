class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        curr = ans
        for i in nums:
            if curr == float('-inf'):
                curr = i 
                ans = i
                continue
            if i + curr > ans and i + curr > i:
                curr += i
            elif i >= curr :
                curr = i
            else:
                curr += i
            ans = max(ans,curr)
        return ans
