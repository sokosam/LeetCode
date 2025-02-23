class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        

        ans = 0
        overall = []
        cols = len(grid[0])
        for row in range(len(grid)):
            for col in range(cols):
                grid[row][col] = -grid[row][col]
            heapq.heapify(grid[row])
            for i in range(limits[row]):
                heapq.heappush(overall, heapq.heappop(grid[row]))
        

        for i in range(k):
            ans += -heapq.heappop(overall)
        return ans