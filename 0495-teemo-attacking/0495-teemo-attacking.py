class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        prev = timeSeries[0]
        total = duration

        for i in range(1,len(timeSeries)):

            if timeSeries[i] - duration < prev:
                total += (timeSeries[i] - prev)
            else:
                total += duration
            
            prev = timeSeries[i]
        return total