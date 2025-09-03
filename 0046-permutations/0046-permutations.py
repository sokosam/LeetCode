class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        used = set()

        def helper(nums, used, curr):
            nonlocal ans
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return

            for i in nums:
                if i not in used:
                    curr.append(i)
                    used.add(i)
                    helper(nums,used,curr)
                    used.remove(i)
                    curr.pop()
        helper(nums, used, [])
        return ans