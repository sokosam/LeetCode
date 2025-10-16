class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        """

        0,1,2,3,4,5,6

        nums[i] - k*value == 0

        we know that the maximum MEX is the len(nums) - count(nums[i] < 0)


        we can mod every positive num by value:
        1 2 3 1 3
        """

        nums = [i%value for i in nums ]
        count = Counter(nums)
        curr = 0
        for i in range(len(nums)):
            if i not in count:
                return i
            elif count[i] >1:
                if i + value not in count:
                    count[i + value] = count[i] -1
                else:
                    count[i+value] += count[i] - 1
        return len(nums)
