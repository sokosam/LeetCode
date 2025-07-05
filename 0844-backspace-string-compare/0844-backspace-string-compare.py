class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def sim(s):
            stack = []
            for i in s:
                if i == "#" and len(stack) > 0:
                    stack.pop()
                if i != "#":
                    stack.append(i)

            return "".join(stack)
        return sim(s) == sim(t)