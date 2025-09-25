class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        s = []
        ans = [-1]*len(nums)
        original_size = len(nums)
        nums = nums + nums
        for i in range(len(nums)):
            k = i %(original_size )
            if len(s) == 0:
                s.append(k)
            else:
                while s and nums[s[-1]] < nums[k]:
                    curr = s.pop()
                    ans[curr] = nums[k]
                
                s.append(k)
        return ans