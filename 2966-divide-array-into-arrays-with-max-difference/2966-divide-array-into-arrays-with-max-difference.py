class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        """


        """

        nums.sort()

        

        nums = [[nums[3*i], nums[3*i + 1], nums[3*i + 2]] for i in range(len(nums)//3)]

        for j in nums:
            if j[-1] - j[0] > k:
                return []
        return nums
            