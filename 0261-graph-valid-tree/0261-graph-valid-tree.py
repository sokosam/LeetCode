class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = [False] * n
        adj = [[] for _ in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        count = [0]

        def dfs(visited, adj, curr, parent, count):
        
            visited[curr] = True
            count[0] += 1

            for i in adj[curr]:
                if not visited[i]:
                    if dfs(visited,adj, i, curr, count):
                        return True

                elif i != parent:
                    return True
            
            return False
        
        if dfs(visited, adj, 0, -1,count):
            return False
        print(count)
        return False if count[0] != n else True