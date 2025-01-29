class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        gifts = [-x for x in gifts ]
        heapq.heapify(gifts)

        for i in range(k):
            val = -heapq.heappop(gifts)
            val = int(val ** 0.5)
            heapq.heappush(gifts,-val)

        
        return -int(sum(gifts))