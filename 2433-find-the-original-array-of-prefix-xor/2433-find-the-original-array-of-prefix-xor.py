class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        """

        5^7 == 2
        0101 ^ 0111
        0101 ^ 1111

        5^2 == 7

        



        """


        return [pref[0]] + [pref[i]^pref[i-1] for i in range(1,len(pref))]