class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x : x[0])

        for i in range(len(intervals)):
            if i - 1 >= 0 and intervals[i][0] < intervals[i -1][1]:
                return False
        return True