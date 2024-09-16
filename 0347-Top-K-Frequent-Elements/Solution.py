# Completed on: 9/15/2024
# Submission: https://leetcode.com/problems/top-k-frequent-elements/submissions/1391534689/
# Time Complexity: O(n + klogk)
# Space Complexity: O(k)
#   k: Number of unique elements in input array 
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        memoi = {}
        for i in range(len(nums)):
            if nums[i] in memoi:
                memoi[nums[i]] +=1
            else: 
                memoi[nums[i]] = 1
        sorted_memoi = sorted(memoi.items(), key =lambda x:x[1], reverse=True)
        returned = []
        for i in range(k):
            returned.append(sorted_memoi[i][0])
        return returned



# Completed on: 7/12/2023
# Submission: https://leetcode.com/problems/top-k-frequent-elements/submissions/993133139/
# Time Complexity: O(???)
# Space Complexity: O(???) 

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        m = 0
        v = []
        hold = 0
        for i in range(k):
            hold = 0
            m= 0
            for key in d:
                m = max(d[key], m)
                if d[key] >= m:
                    hold = key
            v.append(hold)
            d.pop(hold)
        return v  