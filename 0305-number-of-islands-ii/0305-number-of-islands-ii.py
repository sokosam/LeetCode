class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # Use a parent array of size m*n.
        parent = list(range(m * n))
        isOne = [False] * (m * n)

        def find(i):
            # Your find implementation with path halving is correct.
            while parent[i] != i:
                parent[i] = parent[parent[i]] 
                i = parent[i]
            return i
        
        total = 0
        ans = []
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        for pos in positions:
            x, y = pos[0], pos[1]
            
            # --- FIX: Use correct 1D index calculation ---
            # The index for (x, y) is x * n + y.
            idx = x * n + y

            # If the cell is already land, the count doesn't change.
            if isOne[idx]:
                ans.append(total)
                continue
            
            pars = set()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                
                # Check if neighbor is within bounds.
                if 0 <= nx < m and 0 <= ny < n:
                    # --- FIX: Use consistent index calculation for neighbor ---
                    n_idx = nx * n + ny
                    if isOne[n_idx]:
                        pars.add(find(n_idx))
            
            isOne[idx] = True
            total += 1 - len(pars)
            ans.append(total)
            
            # --- FIX: Union using the correct index `idx` ---
            for par in pars:
                parent[par] = idx
                
        return ans