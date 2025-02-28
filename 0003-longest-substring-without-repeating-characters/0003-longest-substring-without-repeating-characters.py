class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}



        ans = 0

        l = 0
        r = 0

        while r < len(s):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1
            while freq[s[r]] > 1 and l < r:
                freq[s[l]] -= 1
                l += 1
            r += 1
            ans = max(ans, r - l)
        return ans
