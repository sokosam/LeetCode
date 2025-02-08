class NumberContainers:

    def __init__(self):
        self.map = {}
        self.mapHeaps = {}

    def change(self, index: int, number: int) -> None:
        self.map[index] = number
        if number in self.mapHeaps:
            heapq.heappush(self.mapHeaps[number], index)
        else:
            self.mapHeaps[number] = [index]

    def find(self, number: int) -> int:
        if number not in self.mapHeaps:
            return -1
        while len(self.mapHeaps[number]) > 0 and self.map[self.mapHeaps[number][0]] != number: 

            heapq.heappop(self.mapHeaps[number])
        
        return self.mapHeaps[number][0] if len(self.mapHeaps[number]) > 0 else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)