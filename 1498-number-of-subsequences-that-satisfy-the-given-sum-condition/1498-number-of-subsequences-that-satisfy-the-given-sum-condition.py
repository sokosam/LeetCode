class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        nums.sort()
        for idx, i in enumerate(nums):
            if i > target:
                break
            t = target - i
            index = bisect_right(nums,t)
            if index <= idx:
                continue
            ans +=  pow(2,index - idx - 1) % MOD
        return ans% MOD
            