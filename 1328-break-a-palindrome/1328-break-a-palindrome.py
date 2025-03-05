class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""

        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[0: i] + 'a' + palindrome[i +1:]
        
        return palindrome[0 : len(palindrome) - 1] + 'b'