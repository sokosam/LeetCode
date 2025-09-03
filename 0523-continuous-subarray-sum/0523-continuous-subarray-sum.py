class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        

        """
        
        23 25 29 35 42

        5  1  5  5  0


        1 3 15
        1 3 3 
        """

        prefix = 0
        m = {}

        for index, i in enumerate(nums):
            if i == 0:
                if index != 0 and (nums[index-1] == 0 or nums[index - 1] == k):
                    return True
                continue
            prefix += i

            mod = prefix % k
            if mod == 0 and index != 0:
                return True
            
            if mod in m:
                idx = m[mod]
                if index - idx >=2:
                    return True
            else:
                m[mod] = index
        return False