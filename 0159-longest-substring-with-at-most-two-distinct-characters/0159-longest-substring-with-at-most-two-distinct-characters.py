class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        

        """

        eceba

        aaaaaaabbbcbbbbbeeeeee

        """

        numDistinct = 0

        count = defaultdict(int)

        ans ,start =0,0

        for end in range(len(s)):
            count[s[end]] +=1

            if count[s[end]] == 1:
                numDistinct +=1
            
            while numDistinct >2:
                count[s[start]] -=1
                if count[s[start]] == 0:
                    numDistinct -=1
                start +=1
            
            ans = max(ans, end - start + 1)

        return ans