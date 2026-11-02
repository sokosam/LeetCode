class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        """
        1,5
        1,5
        1,5
        2,3
        2,3
        """

        events.sort(key = lambda x : x[0])
        pq = []

        end = max([i[1] for i in events])


        ans, e = 0,0

        for i in range(events[0][0], end + 1):
            while pq and pq[0] < i:
                heappop(pq)
            while e < len(events) and events[e][0] == i:
                heappush(pq, events[e][1])
                e+=1
            if len(pq) > 0:
                heappop(pq)
                ans+=1
            # print(i,pq, ans)
        return ans
            







