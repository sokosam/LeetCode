class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        pq = []
        for index,i in enumerate(nums):
            heapq.heappush(pq,[-i,index])
        ans = []
        while k > 0:
            val= heapq.heappop(pq)
            val[0] = -val[0]
            ans.append(val)
            k -=1
        ans.sort(key = lambda x : x[1])
        ans = [i[0] for i in ans]
        return ans
