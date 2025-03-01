class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()

        l = 0
        for i in range(k + 1 ):
            if i >= len(nums):
                continue
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])

        # print(s)
        r = k + 1
        while r < len(nums):
            s.remove(nums[l])
            if nums[r] in s:
                return True
            s.add(nums[r])

            r +=1
            l +=1
        return False