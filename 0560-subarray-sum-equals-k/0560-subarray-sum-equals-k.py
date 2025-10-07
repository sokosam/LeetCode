class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """

        1 2 3 
        

        """

        seen = defaultdict(int)
        seen[0] =1
        prefix = 0
        ans = 0
        for i in nums:
            prefix += i
            if prefix - k in seen:
                ans += seen[prefix - k]
            seen[prefix] += 1
        return ans
