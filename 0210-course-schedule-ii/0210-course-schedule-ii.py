class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0]*numCourses
        adj =[[] for _ in range(numCourses)]   
        queue = deque()

        for req in prerequisites:
            adj[req[1]].append(req[0])
            indegree[req[0]] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        ans = []
        while queue:
            curr = queue.popleft()

            ans.append(curr)
            
            for i in adj[curr]:
                indegree[i] -=1
                if indegree[i] == 0:
                    queue.append(i)
        
        return ans if len(ans) == numCourses else []
