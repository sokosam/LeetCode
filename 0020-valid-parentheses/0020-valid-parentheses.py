class Solution:
    def isValid(self, s: str) -> bool:
        leftPar = {'[', '(', '{'}
        rightPar = {']',')', '}'}
        stack = []

        for i in s:
            if i in leftPar:
                stack.append(i)
            elif i in rightPar:
                if len(stack) == 0:
                    return False
                val = stack.pop()
                print(val)
                if val == '[' and i != ']' or val == '(' and i != ')' or val == "{" and i != '}':
                    return False
        return True if len(stack) == 0 else False