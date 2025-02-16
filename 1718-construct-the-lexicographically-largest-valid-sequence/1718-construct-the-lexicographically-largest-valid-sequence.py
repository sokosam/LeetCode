class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        """

        2 3 2 1 3
        2 1 2

        2 3 2 4 3 1 1 4

        4 2 3 2 4 3 1

        5 3 1 4 3 5 2 4 2


        """

        used = [False] * (n + 1)
        n = [0] * ( 2*n -  1)
        ans = []
        def helper(nums, used, start):

            while start < len(nums) and nums[start] != 0:
                start += 1
            # print(nums, start)
            if start >= len(nums):
                ans.append(nums)
                return True




            for i in range(len(used) -1, 0 ,-1):
                if not used[i] and i == 1:
                    used[i] = True
                    nums[start] = i
                    if helper(nums, used, start + 1):
                        return True
                    used[i] = False
                    nums[start] = 0
                elif not used[i] and start + i < len(nums) and nums[start + i] == 0:
                    used[i] = True
                    nums[start] = i
                    if i != 1: nums[start + i] = i
                    if helper(nums, used, start + 1):
                        return True
                    used[i] = False
                    nums[start] = 0
                    if i != 1: nums[start +i] = 0

            return False
        
        helper(n, used, 0)
        return ans[0]