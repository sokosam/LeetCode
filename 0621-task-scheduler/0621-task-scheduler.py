class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        


        cooldown = deque()

        m = Counter(tasks)
        x = [ [-m[i], i] for i in m]
        heapq.heapify(x)

        
        time = 0
        while x or cooldown:
            print(x,cooldown)
            if x:
                curr = heapq.heappop(x)
                amount = abs(curr[0])
                item = curr[1]
                amount -=1
                if amount > 0:
                    cooldown.append([time + n, [-amount, item]])
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(x,cooldown.popleft()[1])
            time +=1
        return time