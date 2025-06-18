class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        23 25 29 35 42
        23  2  4  6  7
    %k   5  1  5  5  0 
        """

        if len(nums) < 2:
            return False

        prefix = 0
        m = {}

        for index, i in enumerate(nums):
            prefix += i
            if i == 0:
                if index + 1 < len(nums):
                    if nums[index + 1] % k == 0:
                        return True
                if index != 0:
                    if nums[index - 1] % k == 0:
                        return True
                continue
            mod = prefix % k
            if mod == 0 and index != 0:
                return True
            if mod in m:
                for i in range(len(m[mod]) - 1, -1,-1):
                    if abs(m[mod][i] - index) >= 2:
                        return True
                m[mod].append(index)
            else:
                m[mod] = [index]
        print(m)
        return False
