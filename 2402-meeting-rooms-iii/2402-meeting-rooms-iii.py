class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        
        pqworking = []
        pq = []
        meetings.sort(key = lambda x : x[0])

        count = [0]*n

        for i in range(n):
            heappush(pq, [i,0])

        for start,end in meetings:
            total_time = end - start

            while pqworking and pqworking[0][0] <= start:
                time,room = heappop(pqworking)
                heappush(pq, [room,time])
            if len(pq) == 0:
                time, room = heappop(pqworking)
                count[room]+=1
                heappush(pqworking, (max(time,start) + total_time, room))
            else:
                room,time = heappop(pq)
                heappush(pqworking, (max(start,time) + total_time, room))
                count[room] +=1
        highest = max(count)

        for idx, i in enumerate(count):
            if i == highest:
                return idx




