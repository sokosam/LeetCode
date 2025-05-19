class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        curr = 0
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort(key =lambda x: (x[0], x[1]))

        print(tasks)
        q = []
        q.append([tasks[0][1], tasks[0][2], tasks[0][0]])

        ans = []
        tracker = 1
        while q:
            x = heapq.heappop(q)
            if curr < x[2]:
                curr = x[2]
            ans.append(x[1])
            curr += x[0]
            while tracker < len(tasks):
                if tasks[tracker][0] <= curr or len(q) == 0:
                    heapq.heappush(q,[tasks[tracker][1], tasks[tracker][2], tasks[tracker][0]])
                    tracker += 1
                else:
                    break
        return ans
        