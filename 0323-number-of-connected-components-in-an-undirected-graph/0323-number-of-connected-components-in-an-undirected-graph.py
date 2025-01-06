class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """

        [0, 1, 2, 3, 4]
        [0, 0, 2, 3, 4]
        [0, 0, 0, 3, 4]
        [0, 0, 0, 3, 3]

        """
        par = [i for i in range(n)]

        def join(n1):
            p1 = par[n1]

            while p1 != par[p1]:
                p1 = par[p1]
        
            return p1

        def fix(n):
            if par[n] != n:
                root = join(n)
                while par[n] != n:
                    temp = par[n]
                    par[n] = root
                    n = temp

        for edge in edges:
            n1 = join(edge[0])
            n2 = join(edge[1])

            if n1 < n2:
                par[n2] = n1
                fix(edge[0])
                fix(edge[1])
            else:
                par[n1] = n2
                fix(edge[1])
                fix(edge[0])





        print(par)
        seen = set()
        for i in range(len(par)):
            fix(i)
            if par[i] not in seen:
                seen.add(par[i])

        return len(seen)