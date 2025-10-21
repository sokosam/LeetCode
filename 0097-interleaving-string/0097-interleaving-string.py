class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        """

s1 = "aabc"
s2 = "abad"
s3= "aabadabc"


        """
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        def recurse(ptr1,ptr2,ptr3):
            nonlocal s1,s2,s3
            if ptr3 >= len(s3):
                return True
            if dp[ptr1][ptr2] == 2:
                return False
            elif dp[ptr1][ptr2] == 1:
                print(ptr1,ptr2)
                return True
            possible = False
            if ptr1 < len(s1) and s1[ptr1] == s3[ptr3]:
                possible = possible | recurse(ptr1 + 1, ptr2, ptr3 + 1)
            if ptr2 < len(s2) and s2[ptr2] == s3[ptr3]:
                possible = possible | recurse(ptr1, ptr2 + 1, ptr3+1)
            if possible:
                dp[ptr1][ptr2] = 1
            else:
                dp[ptr1][ptr2] =2
            return possible
        return recurse(0,0,0)
