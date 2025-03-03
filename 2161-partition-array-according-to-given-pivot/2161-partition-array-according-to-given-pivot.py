class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        s1 = []
        s2 = []
        s3 = []
        for i in nums:
            if i < pivot:
                s1.append(i)
            elif i == pivot:
                s3.append(i)
            else:
                s2.append(i)

        i = len(nums) - 1

        while s2:
            val = s2.pop()
            nums[i] = val
            i -=1
        while s3:
            val = s3.pop()
            nums[i] = val
            i-=1
        while s1:
            val = s1.pop()
            nums[i] = val
            i -=1
        return nums