class MinStack:

    def __init__(self):
        self.s = []
        self.mins = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.mins) == 0 or self.mins[-1] >= val:
            self.mins.append(val)
 
    def pop(self) -> None:

        if len(self.mins) > 0 and self.mins[-1] == self.s[-1]:
            self.mins.pop(-1)
            self.s.pop(-1)
        else:
            self.s.pop(-1)
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()