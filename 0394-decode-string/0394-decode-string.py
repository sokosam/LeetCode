class Solution:
    def decodeString(self, s: str) -> str:
        

        stack = []

        index = 0

        def helper(index):
            curr = ""
            num = []
            while index < len(s):
                if s[index].isnumeric():
                    num.append(s[index])
                elif s[index] == '[':
                    stack.append(int("".join(num)))
                    num = []
                    index, val = helper(index + 1)
                    multi = stack.pop()
                    curr += multi*val
                elif s[index] == ']':
                    return index, curr
                else:
                    curr += s[index]
                index+=1
            return index, curr
        
        tindex, test = helper(0)
        return test

