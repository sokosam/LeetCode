class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        

        """

        4   5   6

        4

       

        """
        nums.sort()

        ans = [0]
        seen = {}
        def helper(nums, i, k):

            if i >= len(nums):
                # print(" ")
                ans[0] += 1
                return
            # print(nums[i] )

            if nums[i]- k in seen and seen[nums[i] - k] > 0:
                helper(nums, i + 1, k)
            else:
                if nums[i] in seen:
                    seen[nums[i]] +=1
                else:
                    seen[nums[i]] =1
                helper(nums, i + 1, k)
                seen[nums[i]] -=1
                helper(nums, i + 1, k)
        helper(nums,0,k)
        return ans[0] -1