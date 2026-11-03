class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        m = defaultdict(lambda : float('inf'))
        prefix = [0]
        best = float('-inf')

        for idx, i in enumerate(nums):
            prefix.append(prefix[-1] + i)

        for idx, i in enumerate(nums):

            m[i] = min(m[i], prefix[idx])

            # i + k
            x1 = i + k
        
            # i - k
            x2 = i - k

            x1_min = m.get(x1, None)

            x2_min = m.get(x2, None)

            if x1_min is not None:
                best = max(best, prefix[idx + 1] - x1_min)
            if x2_min is not None:
                best = max(best, prefix[idx + 1] - x2_min)


        if best == float('-inf'):
            return 0
        return best




