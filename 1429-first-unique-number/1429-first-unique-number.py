class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.m = defaultdict(int)
        for i in nums:
            self.add(i)
        
        

    def showFirstUnique(self) -> int:
        while self.q:
            curr = self.q[0]
            if self.m[curr] == 1:
                return curr
            self.q.popleft()
        return -1

        

    def add(self, value: int) -> None:
        if self.m[value] == 0:
            self.q.append(value)
        self.m[value] +=1

        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)