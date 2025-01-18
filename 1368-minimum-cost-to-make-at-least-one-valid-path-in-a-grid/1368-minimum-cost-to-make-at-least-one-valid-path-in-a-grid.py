from collections import deque
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        dp = [[float('inf')] * cols for _ in range(rows)]
        dp[0][0] = 0  # Starting point cost is 0

        q = deque([(0, 0, 0)])  # (row, col, cost)

        while q:
            row, col, cost = q.popleft()
            if dp[row][col] < cost:
                continue  # Skip if we already found a better way to reach this cell
            
            for i, (dr, dc) in enumerate(directions):
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    new_cost = cost if grid[row][col] == i + 1 else cost + 1
                    if new_cost < dp[new_row][new_col]:
                        dp[new_row][new_col] = new_cost
                        if new_cost == cost:  # No cost incurred; append to the front
                            q.appendleft((new_row, new_col, new_cost))
                        else:  # Cost incurred; append to the back
                            q.append((new_row, new_col, new_cost))

        return dp[rows - 1][cols - 1]
