class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        """

            10 20 23 30 36


        """



        for i in range(len(nums)):
            if i == 0: continue
            nums[i] = nums[i-1] + nums[i]

        # print(nums)
        ans = 0
        for i in range(0, len(nums) -1):
            if (2*-nums[i] +nums[-1]) % 2 == 0:
                ans +=1
        return ans