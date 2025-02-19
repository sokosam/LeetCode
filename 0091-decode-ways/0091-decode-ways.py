class Solution:
    def numDecodings(self, s: str) -> int:

        stack =[]

        for i in s:
            if i == "0":
                if len(stack) > 0 and (stack[-1] == '1' or stack[-1] == '2'):
                    stack.pop()
                    stack.append('X')
                else:
                    return 0
            else:
                stack.append(i)

        dp = [0]* len(stack)
        for i in range(len(dp)):
            if i == 0:
                dp[i] = 1
                continue
            if stack[i] == "X":
                dp[i] = dp[i -1]
            elif stack[i - 1] == "1":
                val = 1
                if i -2 >= 0:
                    val = dp[i-2]
                dp[i] = dp[i-1] +val
            elif stack[i-1] == "2" and int(stack[i]) <= 6:
                val = 1
                if i -2 >= 0:
                    val = dp[i-2]

                dp[i] = dp[i-1] +val
            else:
                dp[i] = dp[i -1]

        return dp[-1]
    

        """
        
        1 1 2 3
        11 2 3
        1 12 3
        1 1 23
        11 23


        """