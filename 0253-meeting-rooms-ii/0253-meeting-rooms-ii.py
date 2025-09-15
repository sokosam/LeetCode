class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []

        intervals.sort()
        best = 0
        for interval in intervals:
            while heap and heap[0] <= interval[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap,interval[1])
            best = max(best, len(heap))
        return best