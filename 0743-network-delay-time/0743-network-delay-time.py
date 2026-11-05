class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        best_times = [float('inf')]*(n + 1)
        adj = defaultdict(list)
        pq = []


        for source, target, time in times:
            adj[source].append((target, time))

        heappush(pq, (k, 0))
        best_times[k] = 0

        while pq:
            source, time = heappop(pq)

            if time > best_times[source]:
                continue

            for target, weight in adj[source]:
                if best_times[target] <= time + weight:
                    continue
                best_times[target] = time + weight
                heappush(pq, (target, time + weight))
        

        minimum_time =  max(best_times[1:])
        if minimum_time == float('inf'):
            return -1
        else: return minimum_time
