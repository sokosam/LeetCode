class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        ans = [0]* len(temperatures)
        for idx, val in enumerate(temperatures):
            while s and s[-1][0] < val:
                curr = s.pop()
                ans[curr[1]] = idx - curr[1]
            s.append([val,idx])
        return ans