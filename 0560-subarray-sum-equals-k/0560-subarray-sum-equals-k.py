class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # l = 0
        # r  =0
        # curr = 0
        # ans = 0
        # while r < len(nums):
        #     curr += nums[r]
        #     while curr > k and r != l:
        #         curr -= nums[l]
        #         l += 1
            
        #     if curr == k:
        #         ans +=1
        #     r +=1
        # return ans

        dp = {0 : 1}
        ans = 0
        curr = 0
        for i in nums:
            curr += i
            if curr - k in dp:
                ans += dp[curr - k]

            if curr not in dp:
                dp[curr] = 1
            else:
                dp[curr] +=1

        return ans
        """

        [-1, -1, 1]
        
        0 

        -1 -2 -1 



        """