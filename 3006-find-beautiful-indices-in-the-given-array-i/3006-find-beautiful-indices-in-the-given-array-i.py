class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        


        b_indexes = []
        for i in range(len(s)):
            if s[i : i + len(b)] == b:
                b_indexes.append(i)

        if len(b_indexes) == 0:
            return []

        ans = []
        for i in range(len(s)):
            if s[i: i + len(a)] == a:

                closest = max(bisect_right(b_indexes, i) - 1, 0)

                if abs(b_indexes[closest] - i) <= k:
                    ans.append(i)
                elif closest + 1 < len(b_indexes) and abs(b_indexes[closest + 1] - i) <= k: 
                    ans.append(i)


        return ans