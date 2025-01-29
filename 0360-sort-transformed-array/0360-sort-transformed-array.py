class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        ans = [a*(x*x) +  b*x + c for x in nums ]
        ans.sort()
        return ans