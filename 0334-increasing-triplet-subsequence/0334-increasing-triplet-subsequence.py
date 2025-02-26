class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        m1 = float('inf')
        m2 = float('inf')

        for i in nums:
            # print(m1,m2,i) 
            if i > m1 and i > m2:
                return True
            if i < m1:
                m1 = i
            elif i < m2 and i > m1:
                m2 = i
        return False