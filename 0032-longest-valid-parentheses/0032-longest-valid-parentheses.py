class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
            ()()()
            ((()))

        """
        if len(s) == 0:
            return 0
        dp = [-1]*len(s)
        dp[0] = 0

        def validUpTo(s, i):
            if s[i] == '(':
                return 0
            original = i
            candidates = 0
            stack = []
            ans = 0
            while i >= 0:
                if s[i] == "(":
                    if len(stack) == 0:
                        dp[original] = ans
                        return ans
                    else:
                        stack.pop()
                        candidates += 2
                else:
                    stack.append(")")
                if len(stack) == 0:
                    ans += candidates
                    if i -1 >=0 and dp[i - 1] >= 0:
                        dp[original] = ans + dp[i - 1]
                        return ans + dp[i - 1]
                    else:
                        dp[original] = ans
                        return ans
                i -= 1
            dp[original] = ans
            return ans
        
        ans = 0
        # print(validUpTo(s, 2))
        for i in range(len(s)):
            ans = max(ans, validUpTo(s,i))
        print(dp)
        return ans

