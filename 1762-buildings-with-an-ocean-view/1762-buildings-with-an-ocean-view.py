class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        ans = []
        tallest = 0
        for i in range(len(heights)- 1, -1 ,-1):
            if heights[i] > tallest:
                ans.append(i)
            tallest = max(tallest, heights[i])
        ans.reverse()
        return ans