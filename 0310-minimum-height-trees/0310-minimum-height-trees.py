class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
         

        q = deque()



        adj= [[] for _ in range(n) ] 
        count = [0]*n
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
            count[edge[0]] +=1
            count[edge[1]] +=1


        for i in range(len(count)):
            if count[i] == 1:
                q.append([i,0])

        levels = []
        while q:
            curr = q.popleft()
            node = curr[0]
            level = curr[1]
            if level >= len(levels):
                levels.append([node])
            else:
                levels[level].append(node)
            count[node] = 0
            for x in adj[node]:
                count[x] -=1
                if count[x] == 1:
                    q.append([x, level + 1])

        return levels[-1]



        