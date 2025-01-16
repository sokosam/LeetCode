class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.size = 0
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        else:
            self.map[val] = self.size
            if self.size == len(self.arr):
                self.arr.append(val)
            else:
                self.arr[self.size] = val
            self.size +=1
            return True
        

    def remove(self, val: int) -> bool:
        if self.size <= 0:
            return False
        if val in self.map:
            pos = self.map[val]
            del self.map[val]
            if pos != self.size - 1:
                swap_val = self.arr[self.size - 1]
                self.map[swap_val] = pos
                self.arr[pos] = swap_val
            self.size -=1
            return True
        else:
            return False

        

    def getRandom(self) -> int:
        
        return self.arr[(int(random.random() * self.size))]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()