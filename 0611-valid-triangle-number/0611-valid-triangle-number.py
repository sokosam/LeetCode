class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        a + b > c

        2, 2, 3, 4

        2 

        2, 3, 4

        2 

        3, 4

        n^2*log(n)

        """

        nums.sort()
        ans = 0

        for i in range(len(nums)):
            side1 = nums[i]
            # print("Testing: ",side1)
            for j in range(i + 1, len(nums)):
                side2= nums[j]
                total = side1 + side2
                closest = bisect.bisect_left(nums, total)
                # print("Found: ", side2, closest, j)
                ans += max(closest - j - 1,0)
        return ans


