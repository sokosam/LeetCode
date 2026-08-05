class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        sus = [False]*n
        for outer, inner in invocations:
            adj[outer].append(inner)
        q = deque()


        q.append(k)
        while q:
            curr = q.popleft()
            sus[curr] = True

            for i in adj[curr]:
                if not sus[i]:
                    sus[curr] = True
                    q.append(i)
        
        for i in range(n):
            if not sus[i]:
                for j in adj[i]:
                    if sus[j]:
                        return [k for k in range(n)] 
        
        return [i for i in range(n) if not sus[i]]

                