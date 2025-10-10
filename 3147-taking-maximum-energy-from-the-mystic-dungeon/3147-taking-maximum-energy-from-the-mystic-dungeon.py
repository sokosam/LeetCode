class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        prev = [0]*len(energy)
        ans = float('-inf')
        for i in range(len(energy) + k):
            curr = i - k
            if curr < 0:
                prev[i] = energy[i]
            elif i >= len(prev):
                ans = max(ans, prev[curr])
            else:
                prev[i] = max(prev[curr] + energy[i], energy[i])
        return ans
            