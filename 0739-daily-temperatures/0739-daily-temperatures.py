class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pq = []

        ans = [0]*len(temperatures)

        for idx, i in enumerate(temperatures):
            heapq.heappush(pq, [i,idx])
            while pq and pq[0][0] < i:
                val,num = heapq.heappop(pq)
                ans[num] = idx -num
        return ans