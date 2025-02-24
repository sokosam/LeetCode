class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        adj = [[] for _ in range(len(amount))]
        time = [-1] * len(amount)


        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])


        q = deque()

        visited = [False]*len(amount)
        path = [bob]
        q.append((bob, path))

        while q:
            curr, path = q.popleft()
            visited[curr] = True

            if curr == 0:
                break

            for i in adj[curr]:
                if not visited[i]:
                    q.append((i, path + [i]))
        
        for i in range(len(path)):
            time[path[i]] = i

        # print(time)
        visited = [False]*len(amount)
        def dfs(t, curr, amt):

            visited[curr] = True
            if time[curr] == -1:
                amt += amount[curr]
            elif t < time[curr]:
                amt += amount[curr]
            elif t == time[curr]:
                amt += amount[curr]//2

            ans= float('-inf')
            found= False
            # print(amt, curr, time[curr], t)
            for vert in adj[curr]:
                if not visited[vert]:
                    found = True
                    ans = max(ans, dfs(t + 1, vert, amt))

            if not found:
                return amt
            return ans
        
        return dfs(0,0,0)