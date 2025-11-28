class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        """

        [1,8,1,4,4] k =6

        [1,2,1,4,4]
        Node_0 = 1
        Node_4 = 4
        Node_2 = Node_0 + Node_4 + 1 = 4 + 1 + 1

        """

        if sum(values) % k != 0:
            return 0
        if n ==1:
            return 1 if values[0] % k == 0 else 0
        splitted = set()
        adj = [[] for _ in range(n)]
        seen = set()
        vals = [0]*n
        indir = [0 for _ in range(n)]
        q = deque()
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            indir[edge[0]] +=1
            indir[edge[1]] +=1


        for node in range(n):
            if indir[node] == 1:
                q.append(node)

        ans = 0
        while q:
            curr = q.popleft()
            vals[curr] += values[curr] % k
            vals[curr] %= k

            if vals[curr] == 0:
                ans +=1
            
            for node in adj[curr]:
                indir[node] -=1
                vals[node] += vals[curr]
                if indir[node] == 1:
                    q.append(node)  
        print(vals)
        return ans
        # while q:

        #     curr = q.popleft()
        #     if curr in seen:
        #         continue
        #     vals[curr] += values[curr] % k
        #     val = vals[curr] % k
        #     seen.add(curr)

        #     allowed = False
        #     for node in adj[curr]:
        #         if node not in splitted:
        #             allowed = True
        #         if node not in seen:
        #             vals[node] += val 
        #             q.append(node)
        #     if val  == 0 :
        #         # print(curr)
        #         ans +=1
        #         splitted.add(curr)
        # print(vals)
        # return ans
            
            
