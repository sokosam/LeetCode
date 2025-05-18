class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for i in strs:
            x = "".join(sorted(i))
            if x in m:
                m[x].append(i)
            else:
                m[x] = [i]
        
        x = [m[i] for i in m]
        return x