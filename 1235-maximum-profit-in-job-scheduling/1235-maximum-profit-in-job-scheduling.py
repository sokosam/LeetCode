class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        heap = [i for i in endTime]
        heapify(heap)


        dp = defaultdict(int)
        bestBefore = 0
        # print(heap)

        times = [[startTime[i],endTime[i],profit[i]] for i in range(len(profit))]
        times.sort(key = lambda x : x[0])
        ans = 0
        for i in range(len(startTime)):
            start,end,profits = times[i]

            while heap and heap[0] <= start:
                curr = heappop(heap)
                bestBefore = max(bestBefore, dp[curr])
            # print(bestBefore, i, start, end, profits)
            dp[end] = max(dp[end], bestBefore + profits)
            ans = max(ans, dp[end])
        # print(dp)
        return ans