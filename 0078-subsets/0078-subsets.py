class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def iterate(nums, i, curr):
            if i >= len(nums):
                ans.append(curr)
            else:
                iterate(nums, i +1, curr)
                iterate(nums, i + 1, curr + [nums[i]])
        
        iterate(nums, 0, [])
        return ans