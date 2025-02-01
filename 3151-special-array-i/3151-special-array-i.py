class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        curr = -1

        for i in nums:
            if curr == -1:
                curr = i%2
            else:
                if curr == i%2:
                    return False
                curr = i%2
        return True