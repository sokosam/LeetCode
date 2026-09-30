class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        s = []

        max_depth = 0
        for index,i in enumerate(seq):
            if i == "(":
                s.append(index)
            else:
                max_depth = max(max_depth, len(s))
                s.pop()


        ans = [0]*len(seq)
        # print(max_depth)
        A_depth = max_depth//2

        for index,i in enumerate(seq):
            if i == "(":
                s.append(index)
            else:
                depth = len(s)
                l_index = s.pop()
                if depth > A_depth:
                    ans[l_index] = 1
                    ans[index] = 1

        return ans



