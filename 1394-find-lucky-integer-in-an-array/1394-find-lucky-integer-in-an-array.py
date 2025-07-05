class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max([-1] + [Counter(arr)[key] for key in Counter(arr) if key == Counter(arr)[key]]) 