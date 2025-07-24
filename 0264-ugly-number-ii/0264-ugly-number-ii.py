class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """ 

        2,3,5

        Un = 2^i * 3^j * 5^k


        1 -> 2,3,5
        2 -> 4,6,10



        """

        pq = [1]

        cnt = 0
        curr = 0
        seen = set()
        while cnt < n:
            print(pq)
            curr = heappop(pq)
            cnt += 1
            if curr*2 not in seen:
                heappush(pq,curr*2)
            if curr*3 not in seen:
                heappush(pq,curr*3)
            if curr*5 not in seen:
                heappush(pq,curr*5)
            seen.add(curr*2)
            seen.add(curr*3)
            seen.add(curr*5)
        return curr