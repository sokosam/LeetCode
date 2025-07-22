class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # 0.5 * age[x] + 7 < age[x] < age[y]

        """
        2(age[y] - 7) > age[x]
        age[y]> age[x]/2 + 7
        age[y] <= age[x]


        """
        ages.sort()
        ans = 0
        n = len(ages)

        for i, x in enumerate(ages):
            lower = bisect_right(ages, 0.5 * x + 7)
            upper = bisect_right(ages, x) - 1

            if upper >= lower:
                ans += upper - lower
        return ans
