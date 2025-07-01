class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        r = len(letters) - 1
        l = 0
        ans = "zz"
        while (l <= r):
            m = l + (r-l)//2
            if letters[m] > target:
                r = m -1 

                ans = letters[m]
            else:
                l = m + 1
        return ans if ans != "zz" else letters[0]