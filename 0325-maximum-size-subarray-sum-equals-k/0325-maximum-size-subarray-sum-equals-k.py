class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """


         1 , 0 , 5, 3, 6

        1 2 1 6 4 7        k =3

        """


        best = 0

        m = {0 : -1 }

        prefix = 0

        for index, i in enumerate(nums):
            prefix += i

            check = prefix - k
            if check in m:
                best = max(index - m[check], best)
            if prefix not in m:
                m[prefix] = index
        return best 