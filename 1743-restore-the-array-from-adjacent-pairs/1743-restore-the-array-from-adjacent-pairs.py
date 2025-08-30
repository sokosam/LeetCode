class Node:
    def __init__(self, val):
        self.val=val
        self.adj = []


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        m = {}

        for i in adjacentPairs:
            first = i[0]
            second = i[1]


            if first not in m:
                m[first] = Node(first)
            first = m[first]

            if second not in m:
                m[second] = Node(second)
            second = m[second]

            first.adj.append(second)
            second.adj.append(first)


        start = None
        for i in m:
            if len(m[i].adj) == 1:
                start = m[i]
                break

        ans = []
        msize = len(m)
        used = set()

        while len(ans) != msize:
            ans.append(start.val)
            used.add(start.val)
            if len(start.adj) == 1:
                start =start.adj[0]
            else:
                first = start.adj[0].val
                second = start.adj[1].val

                if first in used:
                    start = start.adj[1]
                else:
                    start =start.adj[0]


        return ans

                


