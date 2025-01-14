class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stack = []
        seen = set()

        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    stack.append(('(', i))
                else:
                    if len(stack) > 0:
                        found = stack.pop()
                        seen.add(found[1])
                        seen.add(i)



        wilds =0 
        right = 0
        for i in range(len(s)):
            if i in seen:
                continue
            # temp += s[i] if locked[i] == '0' else "w"
            if locked[i] == "0":
                if right > 0:
                    right -= 1
                else:
                    wilds += 1
            else:
                if s[i] == '(':     
                    right += 1
                else:
                    if wilds == 0 and right == 0:
                        return False
                    else:
                        if right > 0:
                            right -=1
                        else:
                            wilds -=1
        return right == 0 and wilds % 2 == 0