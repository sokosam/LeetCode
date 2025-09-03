class Allocator:

    def __init__(self, n: int):
        self.intervals = [[0,n - 1]]
        self.idTracker = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        
        taken = []
        takenIndex = -1
        for index, i in enumerate(self.intervals):
            if i[1] - i[0] + 1 >= size:
                taken = self.intervals[index]
                takenIndex = index
                break
        if takenIndex == -1:
            return -1
        newUsed = [taken[0], taken[0] + size -1]
        leftOver = [taken[0] + size , taken[1]]

        if leftOver[1] >= leftOver[0]:
            self.intervals = self.intervals[0 : takenIndex] + [leftOver]+  self.intervals[takenIndex + 1:]
        else:
            self.intervals = self.intervals[0 : takenIndex] + self.intervals[takenIndex + 1:]
            if len(self.intervals) > 0 and len(self.intervals[0]) == 0:
                self.intervals = []
        
        self.idTracker[mID].append(newUsed)

        return newUsed[0] 



        

    def freeMemory(self, mID: int) -> int:
        
        released = 0


        while self.idTracker[mID]:
            i = self.idTracker[mID].pop()
            self.intervals.append(i)
            released += i[1] - i[0] + 1

        self.intervals.sort(key= lambda x : x[0])

        if len(self.intervals) == 0:
            return released
        temp = [self.intervals[0]]
        for i in range(1, len(self.intervals)):
            if temp[-1][1] >= self.intervals[i][0] -1:
                temp[-1][1] = self.intervals[i][1]
            else:
                temp.append(self.intervals[i])
        self.intervals = temp

        return released
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)


