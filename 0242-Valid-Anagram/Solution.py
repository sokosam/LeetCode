# Completed on: 7/11/2023
# Submission: https://leetcode.com/problems/valid-anagram/submissions/992188356/
# Time Complexity: O(nlogn)
# Space Complexity: O(1) 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False
    
# Completed on: 9/15/2024
# Submission: https://leetcode.com/problems/valid-anagram/submissions/1391529475/
# Time Complexity: O(n)
# Space Complexity: O(1) 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = [0]*26
        word2 = [0]*26
        
        for i in s:
            word1[ord(i) - ord('a')] +=1
        for i in t:
            word2[ord(i) - ord('a')] +=1
        return word1 == word2