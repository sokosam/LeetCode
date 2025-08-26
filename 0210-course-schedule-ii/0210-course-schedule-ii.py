class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indir = [0]* numCourses

        adj = [[] for _ in range(numCourses)] 

        for i in prerequisites:
            indir[i[0]] += 1
            adj[i[1]].append(i[0])
        
        from collections import deque
        q = deque()
        ans = []

        for i in range(len(indir)):
            if indir[i] == 0:
                q.append(i)

        while q:
            curr = q.popleft()
            ans.append(curr)

            for i in adj[curr]:
                indir[i] -=1
                if indir[i] == 0:
                    q.append(i)
        return ans if len(ans) == numCourses else []