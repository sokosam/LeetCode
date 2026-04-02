class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        m = Counter(nums)
        for key in m:
            heappush(h, [-m[key], key])

        ans = []
        while h and k:
            _, best = heappop(h)
            ans.append(best)
            k-=1
        return ans