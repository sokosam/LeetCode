class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        vals = {}
        ans= 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                val = nums[i]* nums[j]
                if val in vals:
                    ans += 4*vals[val]
                # print(val)
                if val in vals:
                    vals[val] += 1
                else:
                    vals[val] = 1
        # print(vals)
        return 2*ans
