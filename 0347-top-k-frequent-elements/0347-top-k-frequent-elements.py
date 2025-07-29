class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """

        1 1 1 
        2 2
        3



        """


        freq = {}

        for i in nums:
            if i  not in freq:
                freq[i] = -1
            else:
                freq[i] -=1
        
        freq = [[freq[i], i] for i in freq]

        heapq.heapify(freq)
        print(freq)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(freq)[1] )
        return ans