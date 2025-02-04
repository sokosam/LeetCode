class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1 
        skipped = set()
        while l < r:
            if nums[l] == nums[r]:
                l +=1 
                r -= 1
            if nums[l] > nums[r]:
                while nums[r] < nums[l]:
                    r -= 1
                    nums[r] += nums[r + 1]
                    skipped.add(r + 1)
            else :
                while nums[r] > nums[l]:
                    l +=1
                    nums[l] += nums[l- 1]
                    skipped.add(l - 1)
        ans = []
        for i in range(len(nums)):
            if i in skipped:
                continue
            ans.append(nums[i])
        return len(skipped)