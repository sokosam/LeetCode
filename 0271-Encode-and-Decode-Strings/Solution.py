# WIP
# Submission: https://leetcode.com/problems/encode-and-decode-strings/description/ Premium only question, done through NeetCode.io
# Time Complexity: 
# Space Complexity: 

class Solution:
    def encode(self, strs: list[str]) -> str:
        new_str = ""
        for i in strs:
            new_str += "$" + str(len(i)) + i
        return new_str

    def decode(self, s: str) -> list[str]:
        str_list = []

        i = 0
        while i < len(s):
            if s[i] == "$":
                ran = int(s[i+1])

                str_list.append(s[i+2: i + 2 + ran + 1])
        
        return str_list