class Solution:
    def doesAliceWin(self, s: str) -> bool:
        """

        aeiou 

        alice can only remove odd
        bob can only remove even => does this imply that Bob can remove a non-empty string that contains no vowels?


        both have to be nonempty
        
        So since he can remove nonempty 0-vowels, for alice to win, she must remove the entire string in her final move

        odd number of vowels some substring, this means she can remove the entire substring 

        and win on the next round
        

        suppose the string contains a even amount of vowels,
        alice can remove an odd amount, which leads to an odd substring of number of vowels.

        if bob removes an even from an odd number, the resultant is still an odd, which means alice can win on the next turn.


        
        """

        if len(s) == 0:
            return False
        
        m = Counter(s)

        vowels =  {'a', 'e', 'i', 'o','u'}

        count = 0

        for i in vowels:
            if i in m:
                count += m[i]
 

        return count > 0