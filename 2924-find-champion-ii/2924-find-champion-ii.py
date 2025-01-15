class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        

        adj = [0] * n
        for i in edges:
            adj[i[1]] +=1
        
        zero = -1 
        for i in range(len(adj)):
            if adj[i] == 0:
                if zero >= 0:
                    return -1
                else:
                    zero = i
        print(adj)
        return zero