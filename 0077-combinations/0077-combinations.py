class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """


        1 2 
        1 3
        1 4
        2 3
        2 4
        3 4             

        """

        ans = []
        def bt(i):
            nonlocal n,k

            if len(i) == k:
                ans.append(i.copy())
                return
            else:
                for j in range(i[-1] + 1, n + 1):
                    i.append(j)
                    bt(i)
                    i.pop()
            return
        for i in range(1, n +1):
            bt([i])
        return ans
                