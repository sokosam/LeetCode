class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        ans = []
        """
                1
                take
                dont take

                    [1]                          []
            [1,2]           [1]              [2]        []
          [1,2,2] [1,2] [1,2]   [1]       [2,2] [2]   [2] []         
            

        """
        
        nums.sort()
        def helper(nums, curr, i):
            nonlocal ans
            if i >= len(nums):
                ans.append(curr)
                return
            
            helper(nums, curr + [nums[i]], i + 1)
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i +=1
            helper(nums, curr, i + 1)
        helper(nums, [], 0)
        return ans
