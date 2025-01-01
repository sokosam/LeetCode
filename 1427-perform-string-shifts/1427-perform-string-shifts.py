class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0

        for i in shift:
            if i[0] == 0:
                total_shift -= i[1]
            else:
                total_shift += i[1]

        size = len(s)
        total_shift %= size

        if total_shift == 0:
            return s

        # abcde -2
        #  cdeab
        if total_shift < 0:
            total_shift*= -1
            return s[total_shift:] + s[:total_shift]

        # abcde 2
        # deabc
        else:
            return s[size - total_shift :] + s[:size - total_shift]