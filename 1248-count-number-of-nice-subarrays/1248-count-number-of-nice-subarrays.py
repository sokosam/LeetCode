class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        

        """

        0 0 0 1 1 1 2 2 2 2

        """

        prefix = [0]

        for i in nums:
            if i%2 == 1:
                prefix.append(1 + prefix[-1])
            else:
                prefix.append(prefix[-1])
        m = Counter(prefix)

        ans = 0
        for i in prefix:
            if i - k in m:
                ans+= m[i-k]
        return ans