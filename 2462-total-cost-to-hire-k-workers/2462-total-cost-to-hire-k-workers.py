class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        if candidates > len(costs)//2:
            return sum(sorted(costs)[0:k])
        
        if k >= len(costs):
            return sum(costs)

        c1  = costs[0:candidates ]  
        c2 = costs[ len(costs) - candidates:]
        queue = deque(costs[candidates: len(costs) - candidates])
        heapq.heapify(c1)
        heapq.heapify(c2)
        ans = 0
        while k > 0:
            if not c1:
                ans += heapq.heappop(c2)
                k-=1
                continue
            if not c2:
                ans += heapq.heappop(c1)
                k-=1
                continue

            if c1[0] <= c2[0]:
                ans += heapq.heappop(c1)
                if queue:
                    heapq.heappush(c1, queue.popleft())
            else:
                ans += heapq.heappop(c2)
                if queue:
                    heapq.heappush(c2, queue.pop())
            k-=1
        return ans