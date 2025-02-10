class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = set()
        fails = set()

        for i in s1.split(" "):
            if i in ans:
                fails.add(i)
                ans.remove(i)
            elif i in fails:
                continue
            else:
                ans.add(i)
        for i in s2.split(" "):
            if i in ans:
                fails.add(i)
                ans.remove(i)
            elif i in fails:
                continue
            else:
                ans.add(i)
        return list(ans)