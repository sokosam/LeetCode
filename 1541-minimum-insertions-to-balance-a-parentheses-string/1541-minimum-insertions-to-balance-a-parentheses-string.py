class Solution:
    def minInsertions(self, s: str) -> int:
        

        prevR = False
        fixed = []
        for i in s:
            if i == "(":
                if prevR:
                    fixed.append(")")
                fixed.append("(")
                prevR = False
            else:
                if prevR:
                    fixed.append("R")
                    prevR = False
                else:
                    prevR = True
        if prevR:
            fixed.append(")")


        ans = 0
        stack = []
        for i in fixed:
            if i == "(":
                stack.append(i)
            elif i == ")":
                if stack:
                    stack.pop()
                    ans +=1
                else:
                    ans +=2
            elif i == "R":
                if stack:
                    stack.pop()
                else:
                    ans+=1
        ans += len(stack)*2
        return ans
            