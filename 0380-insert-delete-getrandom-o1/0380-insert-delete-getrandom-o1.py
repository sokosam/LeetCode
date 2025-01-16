class RandomizedSet:

    def __init__(self):
        self.map = set()
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        else:
            self.map.add(val)
            self.size +=1
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.map:
            self.map.remove(val)
            self.size -=1
            return True
        else:
            return False

        

    def getRandom(self) -> int:
        x = list(self.map)
        
        val = int(random.random() * self.size)
        return x[val]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()