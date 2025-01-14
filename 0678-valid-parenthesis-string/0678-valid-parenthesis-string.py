class Solution:
    def checkValidString(self, s: str) -> bool:
        stackLocked = []
        stackWilds = []

        for i in range(len(s)):
            if s[i] == '*':
                stackWilds.append(i)
            else:
                if s[i] == '(':
                    stackLocked.append(i)
                else:
                    if len(stackLocked) > 0:
                        stackLocked.pop()
                    elif len(stackWilds) > 0:
                        stackWilds.pop()
                    else:
                        return False

        while len(stackLocked) > 0:
            top = stackLocked.pop()
            if len(stackWilds) ==0:
                return False
            top2 = stackWilds.pop()
            if top > top2:
                return False
        return True