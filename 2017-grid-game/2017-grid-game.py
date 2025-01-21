class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        prefix = [0] * len(grid[0])
        suffix = [0] * len(grid[0])


        for i in range(len(grid[0])):
            if i == 0:
                prefix[i] = grid[0][0]
            else:
                prefix[i] = grid[0][i] +  prefix[i - 1]
        
        for i in range(len(grid[0])):
            if i == 0:
                suffix[i] = grid[1][0]
            else:
                suffix[i] = grid[1][i] +  suffix[i - 1]
        
        ans = float('inf')
        print(prefix, suffix)
        for i in range(len(prefix)):
            ans = min(ans , max( prefix[-1] - prefix[i], suffix[i -1 ] if i != 0 else 0))
        return ans




