class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        ans = [0]*len(temperatures)

        for index in range(len(temperatures)):
            
            while s and temperatures[s[-1]] < temperatures[index]:
                curr = s.pop()
                ans[curr] = index - curr
            
            s.append(index)
        return ans