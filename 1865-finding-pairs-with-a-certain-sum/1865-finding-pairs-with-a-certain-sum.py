class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1 = nums1
        self.nums2 = nums2
        self.n2 = Counter(nums2)
        self.n2 = defaultdict(int, self.n2)
    def add(self, index: int, val: int) -> None:
        
        old = self.nums2[index]
        new = self.nums2[index] + val
        self.nums2[index] += val
        self.n2[old]-=1
        self.n2[new] +=1
    def count(self, tot: int) -> int:

        ans = 0
        for i in self.n1:
            if tot - i in self.n2:
                ans += self.n2[tot-i]
        return ans
        
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot) 