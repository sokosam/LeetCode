class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums


    def reset(self) -> List[int]:
        return self.original
        

    def shuffle(self) -> List[int]:
        copy = self.original.copy()
        new = []
        while copy:
            randomNum = randint(0, len(copy) - 1)
            x = copy.pop()
            if randomNum == len(copy):
                new.append(x)
            else:
                num = copy[randomNum]
                copy[randomNum] = x
                new.append(num)
        return new
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()