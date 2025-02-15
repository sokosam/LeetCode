class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []

        for i in s:

            if len(stack) > 0 and i.lower() == i and i.upper() == stack[-1]:
                stack.pop()
            elif len(stack) > 0 and i.upper() == i and i.lower() == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

            