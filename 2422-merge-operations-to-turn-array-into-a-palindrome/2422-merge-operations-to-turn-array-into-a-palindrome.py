class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1 
        cnt = 0
        while l < r:
            if nums[l] == nums[r]:
                l +=1 
                r -= 1
            elif nums[l] > nums[r]:
                while nums[r] < nums[l]:
                    r -= 1
                    nums[r] += nums[r + 1]
                    cnt +=1
            else :
                while nums[r] > nums[l]:
                    l +=1
                    nums[l] += nums[l- 1]
                    cnt +=1
        return cnt