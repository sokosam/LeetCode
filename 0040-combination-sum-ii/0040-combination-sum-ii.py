class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        ans = []
        def helper(nums, curr, i, target):
            nonlocal ans
            if sum(curr) == target:
                ans.append(curr)
                return
            if i >= len(nums):
                return
            if sum(curr) > target:
                return



            helper(nums, curr + [nums[i]], i + 1,target)
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i +=1
            helper(nums, curr , i+1, target)
        
        helper(candidates, [], 0, target)
        ans.sort()
        return ans

        """


        1 2 2 2 5  target =5


                
                    1
            2                   x
         2     x              2      x
    2    x  2    x         2   x   2   x  


        """