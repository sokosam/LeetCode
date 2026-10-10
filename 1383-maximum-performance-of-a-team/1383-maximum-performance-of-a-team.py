class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        vals = [(speed[i], efficiency[i]) for i in range(n)]
        vals.sort(key =lambda x : x[1])
        MOD = 10**9 + 7
        # print(vals)

        largest_k = [0]*n
        heap = []
        current_best_speed = 0
        for i in range(n -1,-1,-1):
            largest_k[i] = current_best_speed 

            heappush(heap, vals[i][0])
            current_best_speed += vals[i][0]

            while len(heap) > k - 1:
                worst = heappop(heap)
                current_best_speed -= worst
        # print(largest_k)
        best = 0
        for i in range(n):
            best = max(best, vals[i][1]*(vals[i][0] +largest_k[i])) 
        return best % MOD

