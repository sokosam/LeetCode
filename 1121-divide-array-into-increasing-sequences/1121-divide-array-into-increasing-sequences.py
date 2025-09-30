class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        h = []
        m = Counter(nums)
        maxSize = max(m.values())

        for i in nums:
            if len(h) < maxSize:
                heappush(h, [i, 1])
            else:
                best = h[0]
                if best == i:
                    return False
                else:
                    x = heappop(h)
                    heappush(h, [i, x[1] + 1])
        
        for i in h:
            if i[1] < k:
                return False
        return True