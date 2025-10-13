class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        """




        """


        nums.sort()

        dp = [[]for _ in range(len(nums))]

        dp[0] = [nums[0]]

        for i in range(len(nums)):

            for j in range(i):
                if nums[i]%nums[j] == 0:
                    if len(dp[j]) >= len(dp[i]):
                        dp[i] = dp[j].copy()
                        dp[i].append(nums[i])
            if len(dp[i]) == 0:
                dp[i] = [nums[i]]
        print(dp)
        best = []
        for i in range(len(dp)):
            if len(dp[i]) > len(best):
                best = dp[i]
        return best