class Solution:

    def __init__(self, w: List[int]):
        self.sum = []
        for i in w:
            if len(self.sum) > 0:
                self.sum.append(self.sum[-1] + i)
            else:
                self.sum.append(i)

    def pickIndex(self) -> int:
        r  = random.randint(1, self.sum[-1])
        print(r)
        return bisect.bisect_left(self.sum, r)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()