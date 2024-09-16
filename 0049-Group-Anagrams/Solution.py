# Completed on: 7/12/2023
# Submission: https://leetcode.com/problems/group-anagrams/submissions/993120020/
# Time Complexity: O(n)
# Space Complexity: O(n) 

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for s in strs:
            curs = "".join(sorted(s))
            if curs in d.keys():
                d[curs].append(s)
            else:
                d[curs] = [s]
        re = []
        for arr in d:
            re.append(d[arr])
        return re