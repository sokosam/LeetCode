class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegree = [0]* numCourses
        adj = [[] for _ in range(numCourses)]

        queue = deque()
        nodesVisited = 0

        for req in prerequisites:
            indegree[req[0]] += 1
            adj[req[1]].append(req[0])

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            nodesVisited +=1
            curr = queue.popleft()

            for i in adj[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        return nodesVisited == numCourses
