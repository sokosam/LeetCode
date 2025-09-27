class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = [i for i in range(m*n )]
        isOne = [False for i in range(m*n)]

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]] 
                i = parent[i]
            
            return parent[i]
        # print(isOne)
        total = 0
        ans = []
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        for pos in positions:
            pars = set()
            x = pos[0]
            y = pos[1]
            idx = x * n + y
            if isOne[idx]:
                ans.append(total)
                continue
            for dx,dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    n_idx = nx * n + ny
                    if isOne[n_idx]:
                        pars.add(find(n_idx))
            # print(x, y, x + (n-1)*y)
            isOne[idx] = True
            total += 1 - len(pars)
            ans.append(total)
            for par in pars:
                parent[par] = idx

        return ans
            

            