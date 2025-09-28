class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = [-i for i in nums]

        heapify(nums)
        while len(nums) >= 3:
            curr = -heappop(nums)
            second = -heappop(nums)
            third = -heappop(nums)

            if second + third > curr:
                return second + third + curr
            else:
                heappush(nums, -second)
                heappush(nums, -third)
        return 0