class Solution:
    def kthCharacter(self, k: int) -> str:
        """
        a
        a b
        ab bc
        abbc bccd
        abbcbccd bccdcdde
        abbcbccdbccdcdde

        0 
        0 1
        0 1 1 2
        0 1 1 2 1 2 2 3
        0 1 1 2 1 2 2 3 1 2 2 3 2 3 3 4 
        """
        def helper(k):
            if k <= 1: return 0
            x = 1
            while k > x:
                x*=2
            return helper(k - x//2) +1
   
        return chr(ord('a')  + helper(k)%26) 
