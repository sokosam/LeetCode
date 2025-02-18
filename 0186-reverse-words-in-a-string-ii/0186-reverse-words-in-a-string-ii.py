class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        

        def reverse(l, r, arr):

            while l < r:
                arr[r], arr[l] = arr[l], arr[r]
                r -=1
                l += 1


        reverse(0, len(s) - 1, s)  

        lastSpace = -1 
        i = 0
        while i < len(s):
            if s[i] == " ":
                reverse(lastSpace + 1, i - 1, s)
                lastSpace = i
            i += 1
        
        reverse(lastSpace + 1, len(s) -1, s)

            