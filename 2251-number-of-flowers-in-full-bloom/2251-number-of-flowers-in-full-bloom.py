class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        """


        1,   3    ,   4    ,9
          1  2          3     4

              6       7     12     13
        1  2       3      4 

        """


        starts = [i[0] for i in flowers]
        ends = [i[1] for i in flowers]
        starts.sort()
        ends.sort()
        ans = []
        for p in people:

            bloomed = bisect.bisect_right(starts, p)
            withered =  bisect.bisect_left(ends, p )
            ans.append(bloomed - withered )
        return ans