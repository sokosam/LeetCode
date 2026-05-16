class Solution:
    def findMin(self, nums: List[int]) -> int:

        dupes = set()
        new_nums = nums.copy()
        nums = []
        for i in new_nums:
            if i not in dupes:
                nums.append(i)
                dupes.add(i)



        if nums[-1] >= nums[0]: return nums[0]


        l = 0
        r = len(nums) -1
        prev = nums[0]
        best = float('inf')
        while l <= r:
            m = l + (r-l)//2
            target = nums[m]
            best = min(best, target)
            if prev > target:
                r = m -1
            else:
                l = m + 1
            prev = target
        return best