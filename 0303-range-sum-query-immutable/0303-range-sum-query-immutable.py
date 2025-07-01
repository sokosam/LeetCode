class NumArray:

    def __init__(self, nums: List[int]):
        self.pref = [0] 
        for i in nums:
            self.pref.append(i + self.pref[-1])


    def sumRange(self, left: int, right: int) -> int:
        return self.pref[right + 1] - self.pref[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)