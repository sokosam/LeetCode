class Solution:
    def removeStars(self, s: str) -> str:
        z = []
        for i in s:
            if i =='*':
                if len(z) == 0:
                    continue
                else:
                    z.pop(-1)
            else:
                z.append(i)

        return "".join(z)