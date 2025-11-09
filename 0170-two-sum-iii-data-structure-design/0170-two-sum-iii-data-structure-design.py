class TwoSum:

    def __init__(self):
        self.m = defaultdict(int)

    def add(self, number: int) -> None:
        self.m[number] +=1

    def find(self, value: int) -> bool:
        ans = False
        for i in self.m:
            if value - i in self.m:
                if value - i == i:
                    ans = self.m[i] >= 2 | ans
                else:
                    return True
        return ans


        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)