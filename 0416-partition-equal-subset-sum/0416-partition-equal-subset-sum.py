class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = set()
        total = 0
        for i in nums:
            total += i
        if total %2 == 1:
            return False
        for i in nums:
            if i == total//2: return True
            for j in dp.copy():
                if j + i == total//2:
                    print(j , i)
                    return True
                dp.add( j +i)
            dp.add(i)
        return False
