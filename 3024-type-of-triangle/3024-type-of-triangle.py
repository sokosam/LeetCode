class Solution:
    def triangleType(self, nums: List[int]) -> str:
        l = nums[0]
        r = nums[1]
        m = nums[2]

        if l + r <= m or m + l <= r or m + r <= l:
            return "none"
        
        s = {l, r, m}
        if len(s) == 1:
            return "equilateral"
        elif len(s) == 2:
            return "isosceles"
        else:
            return "scalene"