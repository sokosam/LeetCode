class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1

        ans = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if dec > 0:
                    dec = 0
                    inc = 2
                else:
                    inc += 1
                ans = max(ans, inc, dec)
            elif nums[i] < nums[i - 1]:
                if inc > 0 :
                    inc = 0
                    dec = 2
                else:
                    dec += 1
                ans = max(ans, dec, inc)
            else:
                inc = 1
                dec = 1
                ans = max(ans,dec, inc)
        return ans if len(nums) != 1 else 1