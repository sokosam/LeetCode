class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        """
        1 5
        push push push push pop pop pop push

        """

        ans = []
        for index, i in enumerate(target):
            if len(ans) == 0:
                diff = i - 1
                ans += ["Push"]*diff
                ans += ["Pop"]*diff
                ans.append("Push")
            else:
                if target[index] == target[index - 1] + 1:
                    ans.append("Push")
                else:
                    diff =  target[index] -target[index -1] -1
                    ans += ["Push"]*diff
                    ans += ["Pop"]*diff
                    ans += ["Push"]
        return ans
