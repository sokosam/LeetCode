class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        """

        x  + reverse(y) = z = reverse(x) + y
        x + y + reverse(x) + reverse(y) = 2z
        x + y = 2z - reverse(x) - reverse(y)


        42 = 24
        42 - 24 = 18

        97 - 79 = 18

        """

        def reversedInt(n):
            x = [i for i in str(n)]
            x.reverse()
            return int("".join(x))
        m = {}
        ans = 0
        for num in nums:
            reverse = reversedInt(num)
            diff =  num - reverse
            if diff in m:
                ans += m[diff]
                m[diff] +=1
            else:
                m[diff] = 1
        return ans % (10**9+7)