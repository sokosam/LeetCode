class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        def helper(nums, target,curr, i):
            nonlocal ans
            if target == sum(curr):
                ans.append(curr)
                return
            if i >= len(nums):
                return
            if sum(curr) > target:
                return
            
            helper(nums, target, curr + [nums[i]], i)
            helper(nums, target, curr, i + 1)
        helper(candidates, target, [] ,0)
        
        return ans