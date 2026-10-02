class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        times = []

        for time in timePoints:
            h = int(time[0:2])
            m = int(time[3:])

            val = h*60 + m
            times.append(val)
        times.sort()




        """
        10

        1, 9
        2


        """
        best = float('inf')
        for i in range(len(times)):
            prev = (i - 1) % len(times)
            next = (i + 1) % len(times)

            best = min(best,  abs(times[prev] - times[i])) 
            if prev > i:
                diff = times[i] + 1440 - times[prev]
                best = min(best, diff)

            best = min(best, abs(times[next] - times[i]))
            if next < i:
                diff = 1440 - times[i]  + times[prev]
                best = min(best, diff)
        return best

        return best
