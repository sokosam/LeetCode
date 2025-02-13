class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """


        1, 2, 3 k= 19

        8 k = 10

        out = 2

        1, 1, 2, 4, 9, k =20

        4, 5, 9, k = 20

        13

        """

        minH = []
        
        for i in range(len(nums)):
            if nums[i] < k:
                heapq.heappush(minH,nums[i])
        
        count = 0
        while len(minH) >= 2:
            val1 = heapq.heappop(minH)
            val2 = heapq.heappop(minH)
            count +=1

            new = 2*min(val1,val2) + max(val1,val2)
            if new < k:
                heapq.heappush(minH, new)
        
        if len(minH) == 1:
            count +=1
        return count
