class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        """

        23, 2, 4 , 6 , 6
        k = 7

        23 25 29 35 41

        23 2 4 6 7 
        k = 6

        23 25 29 35 42

        23 % 6 = 5
        25 % 6 = 1
        29 % 6 = 5

        
        """
        if len(nums) == 1:
            return False
        


        curr = nums[0]
        m = {nums[0] % k : 0}
        for i in range(1, len(nums)):
            curr += nums[i]
            if curr % k == 0 or (curr % k in m and i - m[curr%k]  >= 2 ):
                return True
            if curr % k not in m:
                m[curr% k] = i
        return False
