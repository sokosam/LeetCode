"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """


        """ 

        intervals = []

        for employee in schedule:
            for time in employee:
                intervals.append([time.start, time.end])

        intervals.sort(key = lambda x : x[0])
        if len(intervals) == 0:
            return []
        newIntervals = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] < newIntervals[-1][1]:
                newIntervals[-1][1] = max(newIntervals[-1][1] , intervals[i][1])
            else:
                newIntervals.append(intervals[i])


        ans = []

        for time in range(1, len(newIntervals)):
            right = newIntervals[time][0]
            left = newIntervals[time -1 ][1]
            if right - left == 0:
                continue
            ans.append(Interval(left,right))

        # for employee in schedule:
        #     print(len(employee))
        #     for time in range(1,len(employee)):
        #         freeTime = [employee[time -1].end, employee[time].start]
        #         intervals.append(freeTime)

        # print(intervals)
        return ans