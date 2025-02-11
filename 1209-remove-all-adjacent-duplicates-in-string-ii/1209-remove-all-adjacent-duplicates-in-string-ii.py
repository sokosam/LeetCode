class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # s1 = []
        # s2 = []

        # for i in s:
        #     curr = 1
        #     if len(s1) > 0:
        #         if i == s2[-1]:
        #             curr = s1[-1] + 1
            
        #     s1.append(curr)
        #     s2.append(i)
        #     if curr == k:
        #         for i in range(k):
        #             s1.pop()
        #             s2.pop()
        # return "".join(s2)          

        s1 = []
        for i in s:
            curr = 1
            if len(s1) > 0:
                prev = s1[-1]
                if prev[0] == i:
                    curr = prev[1] + 1

            s1.append([i, curr])
            if curr == k:
                for i in range(k):
                    s1.pop()

        return "".join([x[0] for x in s1])      