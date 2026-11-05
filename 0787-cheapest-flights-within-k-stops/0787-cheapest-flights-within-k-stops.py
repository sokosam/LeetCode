class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        best = {i : { j :float('inf') for j in range(-1, k + 1)} for i in range(n)}
        for i in range(1, k +1):
            best[src][i] = 0
        pq = [(0,k,src)]

        for start,end,cost in flights:
            adj[start].append((end, cost))

        while pq:
            cost,stops_left, curr  = heappop(pq)
            # print(curr, adj[curr])

            if best[curr][stops_left] < cost:
                continue

            if stops_left == -1:
                continue
            
            for next_stop, next_cost in adj[curr]:
                if best[next_stop][stops_left - 1] > cost + next_cost:
                    best[next_stop][stops_left -1] = cost + next_cost
                    heappush(pq, (cost + next_cost, stops_left - 1, next_stop))

        minimum = min(best[dst].values())
        if minimum == float('inf'): return -1
        return minimum
            