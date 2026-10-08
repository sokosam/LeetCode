class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack= []

        removes = set()
        for index,i in enumerate(s):
            if i == "(":
                stack.append(index)
            else:
                if len(stack) == 1:
                    removes.add(index)
                    removes.add(stack.pop())
                else:
                    stack.pop()
        
        return "".join([i if index not in removes else "" for index,i in enumerate(s)])
            