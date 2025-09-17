class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        prev = None



        ans = []
        while nums and k  > 0:
            curr = heapq.heappop(nums)
            if curr == prev:
                continue
            
            ans.append(-curr)
            prev = curr
            k -=1
        return ans
     