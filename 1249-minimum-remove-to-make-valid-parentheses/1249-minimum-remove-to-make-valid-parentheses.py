class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        

        valid = 0

        left = 0

        for i in s:
            if i == "(":
                left +=1
            elif i == ")" and left > 0:
                left -=1
                valid += 1 
        

        ans = []
        right = 0
        for i in s:
            if i == "(":
                if valid > 0:
                    valid -=1
                    right += 1
                    ans.append(i)
            elif i == ")":
                if right > 0:
                    right -=1
                    ans.append(i)
            else:
                ans.append(i)
        return "".join(ans)
                