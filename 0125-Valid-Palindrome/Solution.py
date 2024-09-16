# Completed on: 9/15/2024
# Submission: https://leetcode.com/problems/valid-palindrome/submissions/1391605089/
# Time Complexity: O(n)
# Space Complexity: O(1) 

class Solution:
    def isPalindrome(self, s:str)-> bool:
        l = 0
        r = len(s) - 1
        s  = s.lower()


        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -=1
                continue
            elif s[l] != s[r]:
                return False
            else:
                l+=1
                r-=1
        return True
    
