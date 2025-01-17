class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = derived[0]

        for i in range(1, len(derived)):
            ans ^= derived[i]
        return not ans 
