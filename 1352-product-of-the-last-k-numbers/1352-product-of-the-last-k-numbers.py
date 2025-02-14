class ProductOfNumbers:

    def __init__(self):
        self.s = []
        self.removedLen = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.removedLen += len(self.s)
            self.s = []
        elif len(self.s) > 0:
            self.s.append(num * self.s[-1])
        else:
            self.s.append(num)
        

    def getProduct(self, k: int) -> int:
        # print(self.s)
        if len(self.s) > k: return 0
        if len(self.s)  == k: return self.s[-1]
        else:
            return self.s[-1]//self.s[-k - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)