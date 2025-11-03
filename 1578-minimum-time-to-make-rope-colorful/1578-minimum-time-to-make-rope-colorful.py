class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        ans= 0

        consec = neededTime[0]
        maxConsec = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i -1]:
                consec += neededTime[i]
                maxConsec = max(maxConsec, neededTime[i])
            else:
                ans += consec - maxConsec
                consec = neededTime[i]
                maxConsec = neededTime[i]
            # print(ans ,consec, maxConsec)
        # 
        ans += consec - maxConsec
        return ans
