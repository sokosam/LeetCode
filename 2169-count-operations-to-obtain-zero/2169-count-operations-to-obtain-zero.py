class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while min(num1, num2) >0:
            maxx = max(num1,num2)
            minn = min(num1,num2)

            num1 = maxx - minn
            num2 = minn
            count+=1
        return count