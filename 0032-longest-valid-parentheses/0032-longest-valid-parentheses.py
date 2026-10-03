class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        
        ( () ( ( 
        
        """
        if len(s) == 0:
            return 0

        valid = [False]*len(s)

        stack = []

        for index, i in enumerate(s):
            if i == "(":
                stack.append(index)
                continue

            if len(stack) == 0:
                continue

            closed = stack.pop()

            for j in range(closed, index + 1):
                valid[j] = True
        


        longest = 0
        best = 0
        for i in range(len(s)):
            if valid[i] == True:
                longest += 1
                best= max(longest,best)
            else:
                longest = 0
        return best