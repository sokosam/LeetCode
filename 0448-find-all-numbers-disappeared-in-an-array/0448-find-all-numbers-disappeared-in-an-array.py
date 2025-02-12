class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):

            curr = abs(nums[i]) -1

            if nums[curr] < 0:
                continue
            else:
                nums[curr] = -nums[curr]
        
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans