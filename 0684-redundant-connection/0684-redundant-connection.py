class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # if a cycle between the edges exist there is an redundant connection
        # is it worth to run depth first search? All it will do is validate a cycle's existence
        #

        # Union Find
        # [1, 2, 3, 4, 5]
        # [1, 2, 3, 3, 5]
        # [1, 1, 3, 3, 5]
        # [1, 1, 3, 1, 5] [1, 1, 1, 1, 5]
        # [1, 1, 3, 1, 3] [1, 1, 1, 1, 1]
        # [1, 1, 3, 1, 1]


        parent = [i for i in range(len(edges) + 1)]
        rank = [1 for _ in range(len(edges) + 1)]

        def join(n):
            n = parent[n]
            while n != parent[n]:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n

        def union(n1, n2):
            p1, p2 = join(n1), join(n2)

            if p1 == p2:
                return False
            
            if rank[p1] < rank[p2]: 
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p2] = p1
            return True
        
        for i in edges:
            if not union(i[0], i[1]):
                return i

        