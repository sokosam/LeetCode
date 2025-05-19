class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], x[1]))
        print(intervals)

        prev = None
        ans = 0
        for i in intervals:
            if prev:
                if i[0] == prev[0]:
                    ans +=1
                elif i[0] < prev[1]:
                    ans +=1
                    if i[1] <= prev[1]:
                        prev = i
                else:
                    prev = i
            if not prev:
                prev = i
        return ans
            


        # [1,2] [1,3] [2,3] [3,4]
        # [[1,2]]  