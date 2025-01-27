class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isReachable = [[False for _ in range(numCourses)]  for _ in range(numCourses)]

        q = deque()
        # indir = [0] * numCourses
        # print(indir)
        # print(isReachable)
        adj = [[] for _ in range(numCourses)]

        for i in prerequisites:
            adj[i[1]].append(i[0])
            # indir[i[0]] += 1
        
        for i in range(numCourses):
            q.append(i)
            seen = set()
            while q:
                val =q.popleft()
                isReachable[i][val] = True
                seen.add(val)
                for j in adj[val]:
                    if j not in seen:
                        q.append(j)
            


        # for i in range(len(indir)):
        #     isReachable[i][i] = True
        #     if indir[i] == 0:
        #         q.append((-1,i))
        # print(q)
        # while q:
        #     par, curr = q.popleft()

        #     if par != -1:
        #         for i in range(len(isReachable[curr])):
        #             if isReachable[par][i]:
        #                 isReachable[curr][i] = True
            
        #     for i in adj[curr]:

        #         q.append((curr, i))
                # print
            # if curr == 1:
            #     print(q)
        # print()
        # print(isReachable)
        ans = []
        for pre, val in queries:
            ans.append(isReachable[val][pre])
        return ans