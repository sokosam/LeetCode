class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        heap = [[neededTime[0], colors[0]]]
        ans = 0
        for i in range(1,len(colors)):
            if colors[i] != heap[0][1]:
                while len(heap) > 1:
                    ans += heappop(heap)[0]
                heappop(heap)
            heappush(heap, [neededTime[i], colors[i]])

        while len(heap) > 1:
            ans += heappop(heap)[0]
        return ans