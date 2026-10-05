class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        
        (()()())
        """

        def scoreOuter(s, multiplier):
            if len(s) == 0:
                return 0

            stack = []

            score = 0
            used = set()
            for index,i in enumerate(s):
                if i == "(":
                    stack.append(index)
                else:
                    left =stack.pop()
                    if len(stack) == 0:
                        if abs(index - left) == 1:
                            score += multiplier
                        used.add(index)
                        used.add(left)
            return score + scoreOuter("".join([s[i] for i in range(len(s)) if i not in used]), multiplier*2)
        
        return scoreOuter(s,1)
