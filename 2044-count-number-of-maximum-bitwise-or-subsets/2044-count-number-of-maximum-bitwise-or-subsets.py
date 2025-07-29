class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = 0 

        maxOr = 0
        for i in nums:
            maxOr = maxOr | i

        def bt(nums, curr, i):
            nonlocal ans
            nonlocal maxOr
            if i >= len(nums):
                if curr == maxOr:
                    ans +=1
            else:
                bt(nums, curr,i + 1)
                bt(nums, curr | nums[i], i +1)
        bt(nums,0,0)
        return ans